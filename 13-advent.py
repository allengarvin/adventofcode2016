#!/usr/bin/python

import sys

SEED=1364
DEST=(39,31)

def wall(y, x):
    return len("{:b}".format(x**2 + 3*x + 2*x*y + y + y**2 + SEED).replace("0", "")) % 2
    
def adjacent(pos):
    y, x = pos
    s = set()
    if not wall(y-1, x) and y-1 >= 0:
        s.add( (y-1, x) )
    if not wall(y+1, x):
        s.add( (y+1, x) )
    if not wall(y, x-1) and x-1 >= 0:
        s.add( (y, x-1) )
    if not wall(y, x+1):
        s.add( (y, x+1) )
    return s
       
def main():
    occupied = set( [(1,1)] )

    adj = set( [(1,1)] )
    step = 0

    while DEST not in occupied:
        new_adj = set()
        for i in adj:
            new_adj |= adjacent(i)
        adj = new_adj 
        occupied |= adj
        step += 1
        if step == 50:
            answer2 = len(occupied)

    print "Answer 1:", step
    print "Answer 2:", answer2
            


if __name__ == "__main__":
    main()
