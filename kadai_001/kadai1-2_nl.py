#! /usr/bin/env python3

# とりあえず書くだけ書いてみます

import sys
i = 1
if len(sys.argv) >= 2:
    try:
        f = open(sys.argv[1])
        lines = f.readlines()
        f.close()
        for line in lines:
            print(i, line,)
            i += 1
    except IOError:
        print('Can not open file:', sys.argv[1], '\n')
    else:
        while(True)
            data = sys.stdin.readline()
            print(i, data,)
            i += 1

# だめでした
# 要件をここに書いていきます
# ⽬標: 20-25⾏程度
# 要件1：os.system()でnlコマンドを起動する実装以外が望ましい。
# 要件2：テキストデータは、ファイル名が指定されればファイルから、ファイル名が無ければstdinから読み込む
# 要件3：ファイル名が不正であればエラー処理をする

