#!/usr/bin/python

import sys

def least_block(a, b, blocks):
    least = a
    for c, d in blocks:
        if d >= a and d <= b:
            least = min(least, c)
    return least

def most_block(a, b, blocks):
    most = b
    for c, d in blocks:
        if c >= a and c <= b:
            most = max(most, d)
    return most

def main():
    blocks = map(lambda x: map(int, x.strip().split("-")), open("../advent-2016/20-input.txt").readlines())

    #print blocks
    new_blocks = []
    for a, b in blocks:
        least = least_block(a, b, blocks)
        most = most_block(a, b, blocks)
        if [least, most] not in new_blocks: 
            new_blocks.append( [least,most] )

    blocks = new_blocks
    #print blocks

    new_blocks = []
    for a, b in blocks:
        flag = False
        for c, d in blocks:
            if c <= a and d >= b and (c < a or d > b):
                flag = True
        if flag:
            continue
        new_blocks.append( [a,b] )
    blocks = new_blocks

    new_blocks = []
    for a, b in blocks:
        least = least_block(a, b, blocks)
        most = most_block(a, b, blocks)
        if [least, most] not in new_blocks: 
            new_blocks.append( [least,most] )

    blocks = sorted(new_blocks)

    total = 0
    flag = False
    for i, x in enumerate(blocks[:-1]):
        if blocks[i+1][0] - x[1] - 1 > 0 and not flag:
            print "Answer 1:", x[1] + 1
            flag = True
        total += blocks[i+1][0] - x[1] - 1
    print "Answer 2:", total
        

if __name__ == "__main__":
    main()
