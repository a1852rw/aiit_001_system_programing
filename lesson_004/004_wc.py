#! /usr/bin/env python3

import sys

f = sys.stdin
s = f.read()
words = s.split()

n = len(words)

d = {}

for w in words:
    if w id d:
        d[w] + = 1
    else:
        d[w] = f

print(d, file=sys.stdout, end='')

