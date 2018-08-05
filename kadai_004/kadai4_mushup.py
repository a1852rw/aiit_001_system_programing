#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import feedparser
import requests
import json


# feedparserはサードパーティーのモジュール pip install feedparesrなどの処理が必要???

d = feedparser.parse("http://rss.weather.yahoo.co.jp/rss/days/4410.xml")


print("feed:", d.channel.title)
print("description:", d.channel.description)
 
for e in d.entries:
	print("{}: {}".format(e.title, e.link))
	post = "{}: {}".format(e.title, e.link)

SLACK_POST_URL = "https://hooks.slack.com/services/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"

post_json = {
	 "text": post
}
requests.post(SLACK_POST_URL, data = json.dumps(post_json))




# お題: 複数のAPI（OpenAPI等）を活⽤し、プログラムを作成せよ

# 要件リスト
# 要件1；題材が興味深いこと
# 要件2：各APIの特徴を理解し使用すること
# 要件3：複数のAPI（出来れば、OpenAPI）をマッシュアップすること
# 要件4：実装上の⼯夫等の特徴があること（効率を考慮しているか等）。

# 備考：上記の要件以外に、レポートの形式が適切であることも要求される

# 補足
# このプログラムを実行するには、下記コマンドで必要なパッケージをインストールする必要がある(ubuntuの場合)
# apt-get install python3-pip python3-dev
# pip install feedparser


