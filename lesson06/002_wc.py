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

s = f.road()
s = st.loawer()
s = s.lower()
s = s.replace(',', ' ')
s = s.replace('.', ' ')
s = s.replace('-', ' ')
s = s.replace('_', ' ')
s = s.replace(';', ' ')
s = s.replace(':', ' ')
s = s.replace('"', ' ')
s = s.replace("'", ' ')
s = s.replace('?', ' ')
s = s.replace('!', ' ')
s = s.replace('(', ' ')
s = s.replace(')', ' ')
s = s.replace('/', ' ')

words = s.split()
print("Number of words:", len(words))
print("Top 10 frequent words:")

words = s.split()

print(words)

