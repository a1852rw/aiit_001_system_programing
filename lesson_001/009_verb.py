#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def verb_ing(s):
	if len(s) <= 2:
		return s
	elif s[-3:] == "ing":
		return s + "ly"
	elif len(s) >= 3:
		return s + "ing"

print(verb_ing("hail"))
print(verb_ing("swimming"))
print(verb_ing("do"))

# 要件1：文字列を受け取って、3文字以上であれば、'ing'を付加した文字列列を返すverb_ing関数(h)を書く
# 要件2：既に'ing'で終わっている場合は'ly'を付加する
# 要件3：2文字以下の文字列の場合は変更しない

# 出力1：hailing
# 出力2：swimingly
# 出力3：do
