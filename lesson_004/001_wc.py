#! /usr/bin/env python3

import sys

f = sys.stdin
s = f.read()
words = s.split()

n = len(words)

print(n, file=sys.stdout, end='')

