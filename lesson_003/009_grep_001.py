#!/usr/bin/env python3
# -*- coding; utf-8 -*-

f = open('small.txt','rU')	
pat = "but"	

import re
# まず最初に正規表現操作を行うモジュール「re」をインポートする

f1 = list(f)
f2 = re.compile(pat, re.IGNORECASE)
# ファイルから読み込んだ各行をリスト形式で変数「f1」に格納す
# 「re.compile()」を使い正規表現オブジェクトにコンパイルする。この際「.IGNORERCASE」を使い大文字小文字を無視する設定にする。

for f3 in f1:
	if re.search(f2, f3) != None:
# 	1行ずつ読み込んだ文字列f3の中に正規表現オブジェクトf2が存在する場合 = "but"が見つかった場合
		print(f3)
#		その行を出力する		

		m1 = re.match(f2,f3)
		f4 = re.sub(f2, "***" + str(f3[m1.start():m1.end()]) + "***", f3)
#		抽出した行f3内で文字列f2と一致する部分を探す
# 		文字列f2の開始位置と終了位置を出力しその前後に「***」を追加した文字列と置き換える
		print(f4)	

f.close()

# 要件1：ファイルを読み込み指定された文字列が存在する行だけを出力する
# 要件2：大文字/小文字を無視する
# 要件3：「要件1」とは別に指定された文字列を「***」で強調し出力する
# 要件4：文字列は同じディレクトリにあるファイル「small.txt」から取得する

# 出力1：But at least we are not what we used to be
# 出力2：***But*** at least we are not what we used to be
