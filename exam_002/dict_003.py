#!/usr/bin/env python3
# -*- coding: utf-8 -*-

dict = {"alice":3, "Bob":5, "Dave":4, "Victor":10}

sorted_dict = sorted(dict.items(), key=lambda x:x[0])

print(len(dict.items()))

for (k, v) in sorted_dict:
        print(k, "->" , v)
#        print(len(k))

# 辞書のキー(名前)が短い順に表示するコード(a)を考える
