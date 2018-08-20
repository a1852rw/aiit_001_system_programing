#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def reserve(s):
	return str(s[::-1])

orig = input("Type a phrease: ")
result = reserve(orig)

if orig == result:
	print("** palindrome **")
# 文字列が反転前/後で同じ値になる=回文である
elif orig != result:
	print(result)

# 要件1：reverse関数を作成する
# 要件2：キーボードから受け取った文字列が回文の場合「** palindrome **」と出力する
# 要件3：キーボードから受け取った文字列が回文ではない場合、受け取った文字列を反転して出力する

# 入力1：alice
# 出力1：ecila

# 入力2：anna
# 出力2：** palindrome **
