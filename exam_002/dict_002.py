#!/usr/bin/env python3
# -*- coding: utf-8 -*-

dict = {"alice":3, "Bob":5, "Dave":4, "Victor":10}

sorted_dict = sorted(dict.items(),key=lambda x:-x[1])

for (k, v) in sorted_dict:
        print(k, "->" , v)

# 辞書の値(数値)の大きい順に表示するコード(a)を考える。
