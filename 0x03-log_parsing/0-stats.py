#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys


def prints(d, size):
    """ WWprint the info"""
    print("File size: {:d}".format(size))
    for i in sorted(d.keys()):
        if d[i] != 0:
            print("{}: {:d}".format(i, d[i]))


s = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
       "404": 0, "405": 0, "500": 0}

count = 0
size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            prints(s, size)

        slist = line.split()
        count += 1

        try:
            size += int(slist[-1])
        except:
            pass

        try:
            if slist[-2] in s:
                s[slist[-2]] += 1
        except:
            pass
    prints(s, size)


except KeyboardInterrupt:
    prints(s, size)
    raise
