#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def mix_up(a, b):
	ret = b[:2] + a[2:] +  " " + a[:2] + b[2:]
	return ret

print(mix_up("mix", "pop"))
print(mix_up("apple", "orange"))
print(mix_up("google", "yahoo"))
print(mix_up("socccer", "goal"))


# 要件1：2個の文字列を受け取って、最初の2文字を交換し、空白文字で連接した文字列を返すmix_up関数を書く
# 要件2：時数は最低2文字以上であることを仮定する

# 出力文字列1：pox mip
# 出力文字列2：orple apange
# 出力文字列3：yaogle gohoo
# 出力文字列4：goccer soal
