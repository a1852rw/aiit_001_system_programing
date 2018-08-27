#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def match_ends(li):
	i = 0
	for s1 in li:
		if len(s1) >= 2 and s1[:1] == s1[-1:]:
			i = i + 1
	return i

print(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']))
print(match_ends(['', 'x', 'xy', 'xyx', 'xx']))
print(match_ends(['aaa', 'be', 'abc', 'hello']))


# 要件1：関数match_endsを書く
# 要件2：受け取った文字列のリストの要素のうち、2文字以上で、最初と最後が同じ文字の文字列の数を返す

# 出力1：3
# 出力2：2
# 出力3：1
