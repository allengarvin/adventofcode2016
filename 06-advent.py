#!/usr/bin/python

import sys

def main():
    input = map(lambda x: x.strip(), open("../advent-2016/06-input.txt").readlines())
    freqs = [ dict() for x in range(len(input[0]))]
    for i in input:
        for j, c in enumerate(list(i)):
            if c in freqs[j]:
                freqs[j][c] += 1
            else:
                freqs[j][c] = 1
    code = ""

    print "Answer 1:", "".join(map(lambda x: sorted(x.items(), key=lambda y: y[1])[-1][0], freqs))
    print "Answer 2:", "".join(map(lambda x: sorted(x.items(), key=lambda y: y[1])[0][0], freqs))
        

if __name__ == "__main__":
    main()
