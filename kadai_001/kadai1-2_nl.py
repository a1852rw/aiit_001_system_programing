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
# Print関数に()がついてませんでした、ここで追加します

            i += 1
    except IOError:
        print( 'Can not open file:', sys.argv[1], '\n')
# ここも()がついていません、追加します
    else:
        while(True)
            data = sys.stdin.readline()
            print(i, data,)
# ここも()がついていません追加します
# それぞれ中身は変数なので”などはいらないはずです。
            i += 1
# これで保存して実行してみましょう
