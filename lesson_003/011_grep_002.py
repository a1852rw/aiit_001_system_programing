#!/usr/bin/env python3
# -*- coding; utf-8 -*-

f = open('small.txt','rU')	
pat = "but"	

import re

f1 = list(f)
f2 = re.compile(pat, re.IGNORECASE)

for f3 in f1:
	if re.search(f2, f3) != None:
		print(f3)	

		m1 = re.match(f2,f3)
		f4 = re.sub(f2, "***" + str(f3[m1.start():m1.end()]) + "***", f3)
		print(f4)	

f.close()

# 要件1：ファイルを読み込み指定された文字列が存在する行だけを出力する
# 要件2：大文字/小文字を無視する
# 要件3：「要件1」とは別に指定された文字列を「***」で強調し出力する
# 要件4：文字列は同じディレクトリにあるファイル「small.txt」から取得する

# 追加要件1：通常のUnixコマンドのように、ファイル名をコマンドライン引数で指定できるようにする。
# 追加要件2：ファイル名が省略されたら、標準⼊⼒（stdin）から⼊⼒を受け取るようにする。
# 追加要件3：パターン⽂字列を引数で渡すようにする。

# 出力1：But at least we are not what we used to be
# 出力2：***But*** at least we are not what we used to be

'''
コマンド入力例は下記の通り
$ python grep.py but small.txt
$ cat small.txt | python grep.py but
'''
