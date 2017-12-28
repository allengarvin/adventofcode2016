#!/usr/bin/python

from collections import Counter

def decrypt(x, i):
    if x == "-":
        return " "
    return chr((((ord(x) - 97) + i) % 26) + 97)
    
def main():
    answer2 = None
    input = [x.strip().rsplit("-", 1) for x in open("../advent-2016/04-input.txt").readlines()]

    count = 0
    for lets, cksum in input:
        ck = "".join(map(lambda x: x[0], sorted(Counter("".join(lets.split("-"))).most_common(), key=lambda x: (-x[1], x[0])))[:5]) 
        if "[{cksum}]".format(cksum=ck) in cksum:
            id = int(cksum.split("[")[0])
            msg = "".join(map(lambda x: decrypt(x, id), list(lets)))
            # These are hilarious name storages! I don't think I noticed this last year.
            if "northpole object storage" in msg:
                answer2 = id
            count += id
    print "Answer 1:", count
    print "Answer 2:", answer2

if __name__ == "__main__":
    main()
