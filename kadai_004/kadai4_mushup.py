#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request

from xml.etree.ElementTree import ElementTree
	f = urllib.request.urlopen("http://zip.cgis.biz/xml/zip.php?zn=1500001")
	et = ElementTree(f)
for e in et.getroot():

print(e)

# お題: 複数のAPI（OpenAPI等）を活⽤し、プログラムを作成せよ

# 要件リスト
# 要件1；題材が興味深いこと
# 要件2：各APIの特徴を理解し使用すること
# 要件3：複数のAPI（出来れば、OpenAPI）をマッシュアップすること
# 要件4：実装上の⼯夫等の特徴があること（効率を考慮しているか等）。

# 備考：上記の要件以外に、レポートの形式が適切であることも要求される


