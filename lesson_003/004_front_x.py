#!/usr/bin/env python3
# -*- coding; utf-8 -*-

def front_x(x):
# ここに指定された処理を記述する

print(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']))
print(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']))
print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))


# 要件1：front_x関数を記述する
# 要件2：この関数は受け取った文字列のリストの要素を分類する「x」で始まる文字列と「x以外」で始まる文字列に分類する
# 要件3：分類した文字列を整列(ソート)したリストを返却する

# 出力1：['xaa', 'xzz', 'axx', 'bbb', 'ccc']
# 出力2：['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
# 出力3：['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
