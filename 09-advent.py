#!/usr/bin/python

import re, sys
from parse import parse

pat = re.compile("^(\([0-9]+x[0-9]+\))")

def decompress_simple(input_str):
    p = pat.split(input_str)
    repeat = p[1]

    rest = "".join(p[2:])
    d = parse("({X:d}x{Y:d})", repeat)
    return rest[:d["X"]] * d["Y"], rest[d["X"]:]

def decompress_complex(input_str):
    new_str_cnt = 0

    while len(input_str):
        if pat.match(input_str):
            p = pat.split(input_str)
            repeat = p[1]

            d = parse("({X:d}x{Y:d})", repeat)

            repeat_num = d["Y"]

            repeat_rest = "".join(p[2:])[:d["X"]]
            real_rest = "".join(p[2:])[d["X"]:]

            if "(" in repeat_rest:
                z, y = decompress_complex(repeat_rest)
                new_str_cnt += repeat_num * z
                input_str = y + real_rest
            else:
                new_str_cnt += repeat_num * len(repeat_rest)
                input_str = real_rest
        else:
            new_str_cnt += 1
            input_str = input_str[1:]

    return new_str_cnt, input_str

def main():
    input = open("../advent-2016/09-input.txt").read().strip()

    input_str = input
    new_str = ""
    while len(input_str):
        if pat.match(input_str):
            x, y = decompress_simple(input_str)
            new_str += x
            input_str = y
        else:
            new_str += input_str[0]
            input_str = input_str[1:]

    print "Answer 1:", len(new_str)
    print "Answer 2:", decompress_complex(input)[0]
            


if __name__ == "__main__":
    main()
