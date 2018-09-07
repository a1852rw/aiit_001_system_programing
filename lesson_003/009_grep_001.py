#!/usr/bin/env python3
# -*- coding; utf-8 -*-

f = open('small.txt','rU')	
pat = "but"	

import re

f1 = list(f)
f2 = re.compile(pat, re.IGNORECASE)
f3 = [s for s in f1 if f2 in s]

print(f3)
	
f.close()

# 要件1：ファイルを読み込み指定された文字列が存在する行だけを出力する
# 要件2：大文字/小文字を無視する
# 要件3：「要件1」とは別に指定された文字列を「***」で強調し出力する
# 要件4：文字列は同じディレクトリにあるファイル「small.txt」から取得する

# 出力1：But at least we are not what we used to be
# 出力2：***But*** at least we are not what we used to be
