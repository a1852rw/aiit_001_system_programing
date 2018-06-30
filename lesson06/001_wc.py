#! /usr/bin/env python3

import sys
print(sys.argv, len(sys.argv))

if argc == 1:
    f = sys.stdin
elif argc == 2:
    try:
            f = open(sys.argv[1], "rU")
    except IOErrow:
        sys.exit("wc: &s: No such file or directory" % (sys.argv[1]))
    else:
        sys.exit("usage: wc[file]")



"""
f = sys.stdin
s = f.read()
words = s.split()

n = len(words)

d = {}

for w in words:
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

def foo(s):
    return d[s]
#sorted_keys = sorted(d.keys(), key=foo, reverse=True)

sorted_keys = sorted(d.keys(), key = lambda x: d[x], reverse = True)

i = 0
for k in sorted_keys:
    if i == 20:
     break
    print("{}: {}".format(k, d[k]))
    i += 1

print(d, file=sys.stdout, end=''
