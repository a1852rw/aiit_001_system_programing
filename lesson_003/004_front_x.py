#!/usr/bin/env python3
# -*- coding; utf-8 -*-

def front_x(x):
	s1 = []
	s2 = []
# 	まずは空のリストs1,s2を作成する

	for s in x:
		if s.startswith("x"):
#		対象の文字列がXで始まるとき
			s1.append(s)
#			対象の文字列をリストs1に追加する
		else:
			s2.append(s)
#			それ以外の場合は対象の文字列をリストs2に追加する
		
	return sorted(s1) + sorted(s2)
#	リストs1とリストs2を連結したリストを返却する

print(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']))
print(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']))
print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))

# 要件1：front_x関数を記述する
# 要件2：この関数は受け取った文字列のリストの要素を分類する「x」で始まる文字列と「x以外」で始まる文字列に分類する
# 要件3：分類した文字列を整列(ソート)したリストを返却する

# 出力1：['xaa', 'xzz', 'axx', 'bbb', 'ccc']
# 出力2：['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
# 出力3：['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
