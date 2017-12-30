#!/usr/bin/python

BREAK1=40
BREAK2=400000

def main():
    input = open("../advent-2016/18-input.txt").read().strip()

    width = len(input)

    r = int("".join(map(lambda x: "0" if x == "." else "1", list(input))), 2)
    total = 0
    row = 1

    while True:
        total += width - len(bin(r)[2:].replace("0", ""))
        r = ((r ^ (r>>1)) ^ (r ^ (r<<1))) & (2 ** width - 1)
        if row == BREAK1:
            print "Answer 1:", total
        if row == BREAK2:
            print "Answer 2:", total
            break
        row += 1

if __name__ == "__main__":
    main()
