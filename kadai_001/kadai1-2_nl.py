#! /usr/bin/env python3

import sys
i = 1
if len(sys.argv) >= 2:
# len関数は要素数を取得する。sys.argv変数はコマンドライン引数を取得する。len(sys.argv)で引数の数をカウントできる。
# コマンドライン引数とは、コンピュータのコマンド入力画面(コマンドライン)からプログラムを起動する際に指定するパラメータのこと。
    try:
        f = open(sys.argv[1])
        lines = f.readlines()
        f.close()
        for line in lines:
            print(i, line)
            i = i + 1
    except IOError:
	sys.exit("nl: %s: No such file or directory" % (sys.argv[1]))
else:
    while(i <= len(sys.argv)):
        data = sys.stdin.readline()
            print(i, data)
        i += 1

# ここのWhileの中のコードで引数(この場合は対象ファイルの文字列)がなくなった時点でプログラムが停止するよう設定した。
# 正直よくわからないが要件を満たした動作をしたのでそれで良しとする。

# このコードでは空白行にも行番号が出力される。答え合わせによるとこの動作は間違いとのこと。


# 要件をここに書いていきます
# ⽬標: 20-25⾏程度
# 要件1：os.system()でnlコマンドを起動する実装以外が望ましい。
# 要件2：テキストデータは、ファイル名が指定されればファイルから、ファイル名が無ければstdinから読み込む
# 要件3：ファイル名が不正であればエラー処理をする

# 注：提出時は1行目のシバンを削除した。
# 手伝ってくれた皆さん本当にありがとうございましt。おかげで無事に終わりました。
