#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

builtin = ['cd', 'exit']

def execCd(cmd):
        dir = cmd[3:]
        try:
                os.chdir(dir)
        except:
                print("Directory " + dir + " not found")

def execExit():
        sys.exit()

while True:
        cmd = input("mysh>")
        if cmd.startswith("cd"):
                execCd(cmd)
        elif cmd.startswith("exit"):
                execExit()
        else:
                os.system(cmd)

# お題：以下の仕様のシェル（コマンドインタプリタ）を作成する

# 要件1:cdコマンドを実現する。
# 要件2：exitコマンド（内部コマンド)を実現する
# 要件3：外部コマンドの実⾏（date等）を実現する
# 要件4：パイプ動作を実現する（|で区切られた2つのコマンド)

