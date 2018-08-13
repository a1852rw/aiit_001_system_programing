#! /usr/bin/env python3

import sys

f = sys.stdin
s = f.read()
words = s.split()

n = len(words)

d = {}

for w in words:
    d[w] = 1

print(d, file=sys.stdout, end='')

# この部分は後ほどビデオを見ながら確認すること
