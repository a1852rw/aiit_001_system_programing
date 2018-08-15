#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def first_last(s):
	if len(s) <= 1:
		return ""
	else:
		return s[:2] + s[-2:]

print(first_last("spring"))
print(first_last("hello"))
print(first_last("a"))
print(first_last("abc"))


# 要件1；文字列を受け取って最初と最後の各2文字から作成した文字字列を返すfirst_last関数を書く
# 要件2：文字列の長さが1以下のときは空文字列を返す

# 出力1：spng
# 出力2：helo
# 出力3：abbc
