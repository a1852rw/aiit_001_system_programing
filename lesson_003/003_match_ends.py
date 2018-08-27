#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
def match_ends(li):
	for s1 in li:
		return len(s1)

print(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']))
print(match_ends(['', 'x', 'xy', 'xyx', 'xx']))
print(match_ends(['aaa', 'be', 'abc', 'hello']))
"""

li = ["aba","xyz","aa","bbb"]

for s1 in li:
	print(len(s1))



# 要件1：関数match_endsを書く
# 要件2：受け取った文字列のリストの要素のうち、2文字以上で、最初と最後が同じ文字の文字列の数を返す

# 出力1：3
# 出力2：2
# 出力3：1
