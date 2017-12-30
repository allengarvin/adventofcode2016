#!/usr/bin/python

import os, sys, itertools, string
from parse import parse

def display_discs(discs, tm):
    for d in discs:
        str = "|"
        for n in range(d[1]):
            if n == (d[3] + tm) % d[1]:
                str += " "
            else:
                str += "="
        str += "|"
        print str

def hole(disc, tm):
    return 0 == (disc[3] + tm) % disc[1]

def main(argv):
    discs = []
    for line in open("../advent-2016/15-input.txt"):
        discs.append(map(int, parse("Disc #{} has {} positions; at time={}, it is at position {}.", line)))

    tm = 0
    while True:
        press = True
        for j, d in enumerate(discs):
            if not hole(d, tm + j + 1):
                press = False
        if press == True:
            print "Answer 1:", tm
            break
            #display_discs(discs, tm)
        tm += 1

    discs.append([7,11,0,0])
    tm = 0
    while True:
        press = True
        for j, d in enumerate(discs):
            if not hole(d, tm + j + 1):
                press = False
        if press == True:
            print "Answer 2:", tm
            break
            #display_discs(discs, tm)
        tm += 1
            

if __name__ == "__main__":
    main(sys.argv)
