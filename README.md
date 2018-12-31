# HorribleFeeds

HorribleFeeds is a Flask app for dynamically generating Atom feeds for individual HorribleSubs shows. Only 1080p magnet URIs are served.

```http
GET /<showid>/
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>Some show - HorribleSubs</title>
  <updated>...</updated>
  <id>https://your.domain/path/showid/</id>
  <author>
    <name>HorribleSubs</name>
  </author>
  <link rel="self" type="application/atom+xml" href="https://your.domain/path/showid/"/>
  <link ref="alternate" type="text/html" href="https://horriblesubs.info/shows/some-show/"/>
  <generator uri="https://github.com/fanaticscripter/HorribleFeeds">HorribleFeeds</generator>
  <entry>
    <title>Some Show EP#</title>
    <link rel="alternate" type="application/x-bittorrent" href="magnet:?xt=urn:btih:..."/>
    <id>magnet:?xt=urn:btih:...</id>
    <updated>...</updated>
    <content>...</content>
  </entry>
  ...
</feed>
```

For instance,

```http
GET /347/
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>One Piece - HorribleSubs</title>
  <updated>2018-12-31T02:17:09Z</updated>
  <id>https://your.domain/path/347/</id>
  <author>
    <name>HorribleSubs</name>
  </author>
  <link rel="self" type="application/atom+xml" href="https://your.domain/path/347/"/>
  <link ref="alternate" type="text/html" href="https://horriblesubs.info/shows/one-piece/"/>
  <generator uri="https://github.com/fanaticscripter/HorribleFeeds">HorribleFeeds</generator>
  <entry>
    <title>One Piece 866</title>
    <link rel="alternate" type="application/x-bittorrent" href="magnet:?xt=urn:btih:ITMU6L366QP4CWOBG5LJYBURD7RJEX3T&amp;tr=http://nyaa.tracker.wf:7777/announce&amp;tr=udp://tracker.coppersurfer.tk:6969/announce&amp;tr=udp://tracker.internetwarriors.net:1337/announce&amp;tr=udp://tracker.leechersparadise.org:6969/announce&amp;tr=udp://tracker.opentrackr.org:1337/announce&amp;tr=udp://open.stealth.si:80/announce&amp;tr=udp://p4p.arenabg.com:1337/announce&amp;tr=udp://mgtracker.org:6969/announce&amp;tr=udp://tracker.tiny-vps.com:6969/announce&amp;tr=udp://peerfect.org:6969/announce&amp;tr=http://share.camoe.cn:8080/announce&amp;tr=http://t.nyaatracker.com:80/announce&amp;tr=https://open.kickasstracker.com:443/announce"/>
    <id>magnet:?xt=urn:btih:ITMU6L366QP4CWOBG5LJYBURD7RJEX3T</id>
    <updated>2018-12-23T07:59:59Z</updated>
    <content type="html">&lt;a href=&#34;magnet:?xt=urn:btih:ITMU6L366QP4CWOBG5LJYBURD7RJEX3T&amp;amp;tr=http://nyaa.tracker.wf:7777/announce&amp;amp;tr=udp://tracker.coppersurfer.tk:6969/announce&amp;amp;tr=udp://tracker.internetwarriors.net:1337/announce&amp;amp;tr=udp://tracker.leechersparadise.org:6969/announce&amp;amp;tr=udp://tracker.opentrackr.org:1337/announce&amp;amp;tr=udp://open.stealth.si:80/announce&amp;amp;tr=udp://p4p.arenabg.com:1337/announce&amp;amp;tr=udp://mgtracker.org:6969/announce&amp;amp;tr=udp://tracker.tiny-vps.com:6969/announce&amp;amp;tr=udp://peerfect.org:6969/announce&amp;amp;tr=http://share.camoe.cn:8080/announce&amp;amp;tr=http://t.nyaatracker.com:80/announce&amp;amp;tr=https://open.kickasstracker.com:443/announce&#34;&gt;1080p Magnet&lt;/a&gt;</content>
  </entry>
  ...
</feed>
```

`showid` is an integer that could be extracted from HorribleSubs show pages, e.g., <https://horriblesubs.info/shows/one-piece/>; just search for `hs_showid` in the HTML.
