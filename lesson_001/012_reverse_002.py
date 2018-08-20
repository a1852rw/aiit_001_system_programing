#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def reserve(s):
	return s[::-1]
# 引数「s」に格納されている文字列の最後から1文字ずつさかのぼって要素(文字)を取り出す

orig = "good"
result = reserve(orig)

print(result)


# 要件1：文字列を反転する関数「reverse」を書く

# 出力2：doog
