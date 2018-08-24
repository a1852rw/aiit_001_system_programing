#!/usr/bin/env python3
# -*- coding; utf-8 -*-

def fix_first(s):
	s1 = s[:1]
	return s.replace(s1,"*")

print(fix_first("babble"))
print(fix_first("google"))
print(fix_first("apple"))
print(fix_first("orange"))


# 要件1：fix_first関数を記述する
# 要件2：文字列を受け取り最初の文字と同じ文字を'*'に変更して返却する
# 要件3：最初の文字は変更しない

# 出力1：ba**le
# 出力2：goo*le
# 出力3：apple
# 出力4：orange

