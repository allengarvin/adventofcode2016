#!/usr/bin/python

import sys
from operator import add, mul

def main():
    moves = open("../advent-2016/01-input.txt").read().strip().split(", ")
    dir = 0
    pos = [0,0]

    places_visited = []
    answer2 = None

    movements = [ [-1,0], [0,1], [1,0], [0, -1] ]
    for m in moves:
        if m[0] == "R":
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4
        steps = int(m[1:])
            
        new_places = [ ( pos[0] + movements[dir][0] * x, pos[1] + movements[dir][1] * x ) for x in xrange(1, steps+1) ] 
        pos = map(add, pos, [ x * steps for x in movements[dir] ])
        if not answer2:
            for block in new_places:
                if block in places_visited:
                    answer2 = block
                else:
                    places_visited.append(block)


    print "Answer 1:", abs(pos[0]) + abs(pos[1])
    print "Answer 2:", abs(answer2[0]) + abs(answer2[1])
        


if __name__ == "__main__":
    main()
