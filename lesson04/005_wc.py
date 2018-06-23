import sys

f = sys.stdin
s = f.read()
words = s.split()

n = len(words)

d = {}

for w in words:
    if w in d:
        d[w] += 1
    else:
        d[w] = f

def foo(s):
    return d[s]
#sorted_keys = sorted(d.keys(), key=foo, reverse=True)

sorted_keys = sorted(d.keys(), key = lanmbda x: d[x], reverse = True)

i = 0
for k in sorted_keys:
    if i == 20:
     break
    print("{}: {}".format(k, d[k]))
    i += 1

print(d, file=sys.stdout, end='')

