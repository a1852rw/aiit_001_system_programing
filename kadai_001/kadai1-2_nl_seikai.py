import sys

argc = len(sys.argv)
if argc == 1:
    f = sys.stdin
elif argc == 2:
    try:
        f = open(sys.argv[1], "rU")
    except IOError:
        sys.exit("nl: %s: No such file or directory" % (sys.argv[1]))
else:
    sys.exit("usage: nl [file]")

i = 1
for s in f:
    s = s.rstrip()
    if s:
        print("{:6d}\t{}".format(i, s))
        i += 1
    else:
        print("")

f.close()
