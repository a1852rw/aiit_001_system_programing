#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s1 = "The quick brown fox jumps over te lazy dog."
s2 = s1[:3]
print(s2)

s2 = s1[16:18]
print(s2)

s2 = s1[5:10] + s1[-4:-1]
print(s2)

s2 = s1[:3] + s1[-9:-6] + s1[11:15] + s1[17:19] + s1[-1:]
print(s2)



# 要件1：指定された文字列s1から指定された文字列s2を生成するコードを書く。
# 要件2：文字列の指定は下記の通り。
# 文字列1：The
# 文字列2：fox
# 文字列3：quick dog
# 文字列4：The lazy brown fox.
