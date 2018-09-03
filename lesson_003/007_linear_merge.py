#!/usr/bin/env python3
# -*- coding; utf-8 -*-

def linear_merge(li1,li2):
	li3 = li1 + li2
#	変数「li3」にリスト「li1」と「li2」を結合したリストを代入する(「+」で結合できる)
	
	return sorted(li3)
#	リスト「li3」の要素を整列させて返却する    

print(linear_merge(['aa','xx','zz'],['bb','cc']))	
print(linear_merge(['aa','xx'],['bb','cc','zz']))	
print(linear_merge(['aa','aa'],['aa','bb','bb']))

# 要件1：関数lier_mergeを記述する
# 要件2：昇順(⼩さい順)の2つのリストを受け取る
# 要件3：マージして要素の値で昇順で整列したリストを返却する

# 出力1：['aa','bb','cc','xx','zz']	
# 出力2：['aa','bb','cc','xx','zz']	
# 出力3：['aa','aa','aa','bb','bb']

