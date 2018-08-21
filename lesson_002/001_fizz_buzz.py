#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fb(n):
	if n % 15 == 0 : 
		return "FizzBuzz"
	elif n % 3 == 0:
		return "Fizz"
	elif n % 5 == 0:
		return "Buzz"
	else:
		return ""

i = 1
while i <= 20:
	print(i, fb(i))
	i = i + 1


# 要件1：関数fbを書く
# 要件2：入力値nが5で割り切れるときは入力値と文字列「Buzz」を出力する
# 要件3：入力値nが3で割り切れるときは入力値と文字列「Fizz」を出力する
# 要件4：入力値nが3と5の両方で割り切れるときは入力値と文字列「FizzBuzz」を出力する
