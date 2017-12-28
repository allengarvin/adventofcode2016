#!/usr/bin/python

import sys
from parse import parse

grid = [ [0] * 50 for x in range(6)]

def rect(a, b):
    for j in range(b):
        for i in range(a):
            grid[j][i] = 1

def rotate_row(a, b):
    grid[a] = grid[a][-b:] + grid[a][:-b]

def rotate_column(a, b):
    column = [grid[x][a] for x in range(len(grid))]
    column = column[-b:] + column[:-b]
    for x in range(len(grid)):
        grid[x][a] = column[x]

def display():
    for row in grid:
        print "".join(map(lambda x: "#" if x else ".", row))

def main():
    input = map(lambda x: x.strip(), open("../advent-2016/08-input.txt").readlines())
    parses = [ ("rect {:d}x{:d}", rect ),
               ("rotate row y={:d} by {:d}", rotate_row ),
               ("rotate column x={:d} by {:d}", rotate_column ) ]

    rules = []

    for i in input:
        for par, func in parses:
            p = parse(par, i)
            if p:
                rules.append( [func, p[0], p[1]] )
    cnt = 0
    for r in rules:
        r[0](r[1], r[2])
    print "Answer 1:", sum(map(sum, grid))
    print "Answer 2:"
    display()

if __name__ == "__main__":
    main()
