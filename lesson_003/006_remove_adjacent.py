#!/usr/bin/env python3
# -*- coding; utf-8 -*-

def remove_adjacent(li):
	if len(li) != 0:
		n1  = []
		n1.append(li[0])
		for i in range(1, len(li)):
			if li[i] != li[i - 1]:
				n1.append(li[i])
			return n1
	else:
		return li
			
print(remove_adjacent([1,2,2,3]))	
print(remove_adjacent([2,2,3,3,3]))	
print(remove_adjacent([]))

# 要件1：remove_adjacent関数を記述する
# 要件2：リストを受け取り隣接した要素が同じだった場合にその要素を削除する
# 要件3：処理の後に値を返却する

# 出力1：[1,2,3]
# 出力2：[2,3]
# 出力3：[]
