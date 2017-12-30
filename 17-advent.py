#!/usr/bin/python

import sys

def step(a):
    return a + "0" + a[::-1].replace("0", "X").replace("1", "0").replace("X", "1")

def cksum(a):
    return "".join(map(lambda x: "1" if x[0] == x[1] else "0", [a[i:i+2] for i in range(0, len(a), 2)]))

def transform(istr, ilen):
    while len(istr) < ilen:
        istr = step(istr)
    istr = istr[:ilen]

    c = cksum(istr)
    while len(c) % 2 == 0:
        c = cksum(c)
    return c

def main():
    print "Answer 1:", transform("01000100010010111", 272)
    print "Answer 1:", transform("01000100010010111", 35651584)
    

if __name__ == "__main__":
    main()
