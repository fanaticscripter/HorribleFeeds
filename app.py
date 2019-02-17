#!/usr/bin/env python3

import datetime
import re
import time
import urllib.parse

import arrow
import bs4
import flask
import requests

from preset import KNOWN_SHOWS


app = flask.Flask(__name__)


class Episode:
    def __init__(self, title, date, magnet_link):
        self.title = title
        self.date = date
        self.magnet_link = magnet_link

    @property
    def show_title(self):
        return re.sub(r" \d+$", "", self.title)

    @property
    def btih(self):
        return re.search(r"urn:btih:(?P<btih>\w+)\b", self.magnet_link).group("btih")

    @property
    def abbreviated_magnet_link(self):
        return f"magnet:?xt=urn:btih:{self.btih}"

    @property
    def updated(self):
        return min(
            # Since HorribleSubs getshows API doesn't have time
            # granularity greater than the date, we use the last second
            # of the date in PST (timezone used by HorribleSubs
            # website), provided that it doesn't exceed the current
            # time.
            arrow.now(),
            arrow.get(self.date, "US/Pacific").shift(days=1, seconds=-1),
        )


@app.template_filter("iso8601")
def format_iso8601(datetime):
    return datetime.to("utc").replace(microsecond=0).isoformat().replace("+00:00", "Z")


@app.route("/<int:showid>/")
def feed(showid):
    show_url = None
    for url, sid in KNOWN_SHOWS:
        if sid == showid:
            show_url = urllib.parse.urljoin("https://horriblesubs.info/", url)
    episodes = get_episodes(showid)
    if episodes:
        show_title = episodes[0].show_title
    else:
        if show_url:
            # No episodes for a known show. The scraper is probably
            # broken.
            flask.abort(500)
        show_title = "Unknown"
    resp = flask.make_response(
        flask.render_template(
            "feed.atom",
            showid=showid,
            show_url=show_url,
            title=f"{show_title} - HorribleSubs",
            updated=arrow.now(),
            episodes=episodes,
        )
    )
    resp.headers["Content-Type"] = "application/atom+xml; charset=utf-8"
    return resp


# Returns a list of (title, date, magnet_link).
def get_episodes(showid):
    timestamp = int(time.time() * 1000)
    api_url = f"https://horriblesubs.info/api.php?method=getshows&type=show&showid={showid}&nextid=0&_={timestamp}"
    soup = bs4.BeautifulSoup(requests.get(api_url, timeout=5).text, "html.parser")
    episodes = []
    for container in soup.select(".rls-info-container"):
        label = container.select_one(".rls-label")
        date = label.select_one(".rls-date").text.strip()
        if date == "Today":
            date = arrow.now().to('US/Pacific').date()
        else:
            date = datetime.datetime.strptime(date, "%m/%d/%y").date()
        for span in label.select("span"):
            span.extract()
        title = label.text.strip()
        a_magnet = container.select_one(".rls-link.link-1080p .hs-magnet-link a")
        if a_magnet:
            episodes.append(Episode(title, date, a_magnet["href"]))
    return episodes


def main():
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.jinja_env.auto_reload = True
    app.run(debug=True, threaded=True)


if __name__ == "__main__":
    main()
