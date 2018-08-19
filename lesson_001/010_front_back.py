#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def front_back(a, b):
	a1 = len(a)
	b1 = len(b)
	a2 = int(len(a) / 2)
	b2 = int(len(b) / 2)
	# ここでintで型変換を行わないと文字列の取得でエラーが発生する

	if a1 % 2 == 0 and b1 % 2 == 0:
		return a[:a2] + b[:b2] + a[-a2:] + b[-b2:]
	# aとbが偶数の場合
	
	elif a1 % 2 == 0 and b1 % 2 != 0:
		return a[:a2] + b[:b2+1] + a[-a2:] + b[-b2:]
	# aが偶数でbが奇数の場合	

	elif a1 % 2 != 0 and b1 % 2 == 0:
		return a[:a2+1] + b[b2] + a[-a2:] + b[-b2:]
	# aが奇数でbが偶数の場合

	elif a1 % 2 != 0 and b1 % 2 != 0:
		return a[:a2+1] + b[:b2+1] + a[-a2:] + b[-b2:]
	# aとbが奇数の場合

print(front_back('abcd', 'xy'))
print(front_back('abcde', 'xyz'))
print(front_back('Kitten', 'Donut'))

# 要件1：2つの文字列aとbを受け取り値を返却する
# 要件2：関数front_backを作成しその中で文字列を処理する
# 要件3：返却する文字列は「aの前半」＋「bの前半」＋「aの後半」＋「bの後半」とする
# 要件4：関数front_back内では受け取った文字列を2分割する
# 要件5：文字列の長さが偶数であれば真ん中で分割する
# 要件6：文字列の長さが奇数であれば、前の部分文字列を1文字多くする

# 出力1：abxcdy
# 出力2：abcxydez
# 出力3：KitDontenut
