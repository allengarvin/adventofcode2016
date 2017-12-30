#!/usr/bin/python

import sys
from hashlib import md5

SALT="ihaygndm"
#SALT="abc"

PROBLEM=1

def main():
    n3 = {hex(x)[2]: [] for x in range(16)}
    n5 = {hex(x)[2]: [] for x in range(16)}
    
    i = 0
    while True:
        tmpsalt = "%s%d" % (SALT, i)
        if PROBLEM == 2:
            for j in range(2017):
                hash = md5(tmpsalt).hexdigest()
                tmpsalt = hash
        else:
            hash = md5(tmpsalt).hexdigest()

        threes = []
        for s in n3.keys():
            s3 = s * 3
            s5 = s * 5 

            if s3 in hash:
                threes.append(hash.index(s3))
            if s5 in hash:
                n5[s].append(i)
        if len(threes):
            n3[hash[min(threes)]].append(i)

        i += 1
        if i == 25000:
            break

    keys = []

    for k,v in n5.iteritems():
        for v5 in v:
            for v3 in n3[k]:
                if v3 >= v5 - 1000 and v3 < v5 and v3 not in keys:
                    keys.append(v3)

    #print "\n".join(map(lambda x: "%5d %s" % (x, md5("%s%d" % (SALT, x)).hexdigest()), sorted(keys)[:64]))
    print "Answer %d:" % PROBLEM, sorted(keys)[63]
    

if __name__ == "__main__":
    main()
