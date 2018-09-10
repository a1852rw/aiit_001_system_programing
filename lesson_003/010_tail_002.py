#!/usr/bin/env python3
# -*- coding; utf-8 -*-

f = open('small.txt','rU')

f1 = list(f)
for line in reversed(f1):
	print(line, end='')
f.close()

# 要件1：ファイル「small.txt」を読み込む
# 要件2：読み込んだファイルを後ろの⾏から表⽰する
# 注：ファイル「small.txt」は同じディレクトリに保存してある

# 追加要件1：通常のUnixコマンドのように、ファイル名をコマンドライン引数で指定できるようにする。
# 追加要件2：ファイル名が省略されたら、標準⼊⼒（stdin）から⼊⼒を受け取るようにする。


'''
出力する文字列
-- Football Coach	
But at least we	are not	what we	used to be
We are not what	we need	to be
We are not what	we should be
'''

'''
コマンド入力例は下記の通り
$ python tail.py small.txt
$ cat small.txt | python tail.py
'''
