#! /usr/bin/env python3

import sys
i = 1
if len(sys.argv) >= 2:
    try:
        f = open(sys.argv[1])
        lines = f.readlines()
        f.close()
        for line in lines:
            print i, line,
            i += 1
except IOError:
        print 'Can not open file:', sys.argv[1], '\n'
else:
    while(True)
        data = sys.stdin.readline()
        print i, data,
        i += 1
