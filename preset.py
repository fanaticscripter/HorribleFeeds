# List of current season shows (fetched 12/30/2018).
#
# If any show on this list returns blank, the scraper is probably
# broken, and we should be noisy about it.
#
# curl -s https://horriblesubs.info/current-season/ | \
#     grep -Po '/shows/[^"]+' | \
#     sed 's:$:/:' | \
#     while read show_url; do \
#         echo "('$show_url', $(curl -sL https://horriblesubs.info$show_url | grep -Po '(?<=hs_showid = )\d+')),"
#         sleep 1
#     done
KNOWN_SHOWS = [
    ('/shows/ace-attorney-s2/', 1173),
    ('/shows/akanesasu-shoujo/', 1155),
    ('/shows/anima-yell/', 1181),
    ('/shows/bakumatsu/', 1163),
    ('/shows/banana-fish/', 1112),
    ('/shows/beelzebub-jou-no-okinimesu-mama/', 1190),
    ('/shows/black-clover/', 959),
    ('/shows/bonobono/', 694),
    ('/shows/boruto-naruto-next-generations/', 869),
    ('/shows/cardfight-vanguard-2018/', 1101),
    ('/shows/chuukan-kanriroku-tonegawa/', 1109),
    ('/shows/conception/', 1186),
    ('/shows/dakaretai-otoko-1-i-ni-odosarete-imasu/', 1168),
    ('/shows/detective-conan/', 97),
    ('/shows/double-decker-doug-and-kirill/', 1147),
    ('/shows/fairy-tail-final-season/', 1179),
    ('/shows/gaikotsu-shotenin-honda-san/', 1183),
    ('/shows/gakuen-basara/', 1172),
    ('/shows/gegege-no-kitarou-2018/', 1058),
    ('/shows/goblin-slayer/', 1175),
    ('/shows/golden-kamuy/', 1090),
    ('/shows/gurazeni/', 1074),
    ('/shows/himote-house/', 1182),
    ('/shows/hinomaru-sumo/', 1166),
    ('/shows/irozuku-sekai-no-ashita-kara/', 1171),
    ('/shows/jingai-san-no-yome/', 1158),
    ('/shows/jojos-bizarre-adventure-golden-wind/', 1169),
    ('/shows/karakuri-circus/', 1188),
    ('/shows/kaze-ga-tsuyoku-fuiteiru/', 1159),
    ('/shows/ken-en-ken-aoki-kagayaki/', 1157),
    ('/shows/kishuku-gakkou-no-juliet/', 1170),
    ('/shows/kitsune-no-koe/', 1193),
    ('/shows/merc-storia-mukiryoku-shounen-to-bin-no-naka-no-shoujo/', 1187),
    ('/shows/one-piece/', 347),
    ('/shows/ore-ga-suki-nano-wa-imouto-dakedo-imouto-ja-nai/', 1185),
    ('/shows/radiant/', 1174),
    ('/shows/release-the-spyce/', 1178),
    ('/shows/rerided-tokigoe-no-derrida/', 1151),
    ('/shows/saint-seiya-saintia-shou/', 1195),
    ('/shows/seishun-buta-yarou-wa-bunny-girl-senpai-no-yume-wo-minai/', 1161),
    ('/shows/senran-kagura-shinovi-master-tokyo-youma-hen/', 1191),
    ('/shows/shounen-ashibe-go-go-goma-chan/', 667),
    ('/shows/sora-to-umi-no-aida/', 1160),
    ('/shows/souten-no-ken-re-genesis/', 1062),
    ('/shows/ssss-gridman/', 1177),
    ('/shows/sword-art-online-alicization/', 1176),
    ('/shows/tensei-shitara-slime-datta-ken/', 1152),
    ('/shows/the-idolmster-side-m-wake-atte-mini/', 1184),
    ('/shows/thunderbolt-fantasy-s2/', 1154),
    ('/shows/toaru-majutsu-no-index-iii/', 1189),
    ('/shows/tokyo-ghoul-re/', 1068),
    ('/shows/tonari-no-kyuuketsuki-san/', 1164),
    ('/shows/tsurune/', 1192),
    ('/shows/uchi-no-maid-ga-uzasugiru/', 1167),
    ('/shows/uchuu-senkan-tiramisu-s2/', 1156),
    ('/shows/ulysses-jeanne-darc-to-renkin-no-kishi/', 1180),
    ('/shows/yagate-kimi-ni-naru/', 1165),
    ('/shows/yu-gi-oh-vrains/', 901),
    ('/shows/zombieland-saga/', 1162),
]
