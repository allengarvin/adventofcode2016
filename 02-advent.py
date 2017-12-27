#!/usr/bin/python

import sys
from operator import add

def execute(grid, input):
    for k, v in grid.iteritems():
        if v == "5":
            pos = list(k)
    movements = { "U" : (-1,0), "D" : (1,0), "L": (0,-1), "R" : (0, 1) }

    combination = []
    for line in input:
        for seq in line:
            new_pos = map(add, pos, movements[seq])
            if tuple(new_pos) in grid:
                pos = new_pos
        combination.append(grid[tuple(pos)])
    return combination


def main():
    input = map(lambda x: list(x.strip()), open("../advent-2016/02-input.txt").readlines())
    grid = dict([tuple([x / 3, x % 3]), str(x+1)] for x in xrange(0,9))

    print "Answer 1:", "".join(execute(grid, input))

    y_pos = [ 0, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4 ]
    x_pos = [ 2, 1, 2, 3, 0, 1, 2, 3, 4, 1, 2, 3, 2 ]

    grid = dict()
    for i in range(0, 13):
        grid[(y_pos[i], x_pos[i])] = "%X" % (i+1)
    print "Answer 2:", "".join(execute(grid, input))
    
            
if __name__ == "__main__":
    main()
