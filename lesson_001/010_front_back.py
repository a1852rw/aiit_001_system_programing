#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def front_back(a, b):
	a1 = int(len(a))
	b1 = len(b)
	a2 = len(a) / 2
	b2 = len(b) / 2

        return a[:a1]
#	return a[:a2] + b[:b2] + a[-a2:] + b[-b2:]

#	if a1 % 2 == 0 and b1 % 2 == 0:
#		return a[: a2] + b[: b2] + a[-a2 :] + b[-b2 :]

print(front_back('abcd', 'xy'))
print(front_back('abcde', 'xyz'))
print(front_back('Kitten', 'Donut'))

# 要件1：2つの文字列a及びbを受け取って、aの前＋bの前＋aの後＋bの後から構成される文字列を返すfront_back関数を書く
# 要件2：受け取った文字列は2分割する。
# 要件3：文字列の長さが偶数であれば真ん中で分割する
# 要件4：文字列の長さが奇数であれば、前の部分文字列を1文字多くする。

# 出力1：abxcdy
# 出力2：abcxydez
# 出力3：KitDontenut
