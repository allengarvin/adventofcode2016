#!/usr/bin/python

import sys

def main():
    input = map(lambda x: map(int, x.split()), open("../advent-2016/03-input.txt").readlines())

    print "Answer 1:", len(filter(lambda x: x[2] < x[0] + x[1], map(lambda x: sorted(x), input)))

    triangles = []
    for i in range(0, len(input), 3):
        triangles += [
             sorted([ input[i][0], input[i+1][0], input[i+2][0] ]),
             sorted([ input[i][1], input[i+1][1], input[i+2][1] ]),
             sorted([ input[i][2], input[i+1][2], input[i+2][2] ]),
        ]
    print "Answer 2:",  len(filter(lambda x: x[2] < x[0] + x[1], triangles))

if __name__ == "__main__":
    main()
