#!/usr/bin/python

import sys, re

def detect_tls(s):
    for i in xrange(len(s[:-3])):
        word = s[i:i+4]
        if word[0] != word[1] and word[0] == word[3] and word[1] == word[2]:
            return word
    return None
        
def detect_ssl(outside, inside):
    for p in outside:
        for i in xrange(len(p[:-2])):
            word = p[i:i+3]
            if word[0] != word[1] and word[0] == word[2]:
                if filter(lambda x: ("%s%s%s" % (word[1],word[0],word[1])) in x, inside):
                    return True
    
def main():
    input = map(lambda x: x.strip(), open("../advent-2016/07-input.txt").readlines())
    outside = re.compile("([^[\]]+)(?:$|\[)")
    inside = re.compile("\[([^[\]]+)\]")
    cnt = 0
    cnt2 = 0
    for l in input:
        o = outside.findall(l)
        i = inside.findall(l)
        if filter(detect_tls, o) and not filter(detect_tls, i):
            cnt += 1
        if detect_ssl(o, i):
            cnt2 += 1
    
    print "Answer 1:", cnt
    print "Answer 2:", cnt2
        

if __name__ == "__main__":
    main()
