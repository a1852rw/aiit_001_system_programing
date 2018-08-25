#!/usr/bin/env python3
# -*- coding; utf-8 -*-

def not_bad(s):
	n = "not"
	b = "bad"
	g = "good"
	
	if s.find(n) != -1 and s.find(b) != -1 and s.find(n) < s.find(b):
		return s[:s.find(n)] + "good" + s[s.rfind(b)+3:]
	else:
		return s

print(not_bad('This movie is not so bad'))
print(not_bad('This dinner is not that bad!'))
print(not_bad('This tea is not hot'))
print(not_bad("It's bad yet not"))


# 要件1：not_bad関数を作成する
# 要件2：受け取った文字列の中の「not」の後に「bad」が現れたら「not」から「bad」までの文字列を「good」で置換する

# 出力1：This movie is good
# 出力2：This dinner is good!
# 出力3：This tea is not hot
# 出力4：It's bad yet not


