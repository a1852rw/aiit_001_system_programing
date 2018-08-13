#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("hello", 123)
# この場合は引数を空白文字で区切って表示してくれる 

print("hello" + 123) 
# この場合は異なるデータ型とみなされエラーが発生する

print("hello", end='')
#"この場合は引数「end=''」により自動改行が抑制される。エラーにはならない。

