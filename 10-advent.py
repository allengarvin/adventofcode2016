#!/usr/bin/python

import sys
from parse import parse
from operator import mul

def bot_holding(bots):
    return filter(lambda x: len(bots[x]) == 2, bots.keys())

def main():
    input = map(lambda x: x.strip(), open("../advent-2016/10-input.txt").readlines())
    initials = filter(lambda x: "goes to bot" in x, input)
    cmds = filter(lambda x: " gives " in x, input)

    bots = dict()

    for i in initials:
        p = parse("value {value:d} goes to bot {bot:d}", i)

        b = p["bot"]
        v = p["value"]

        if b in bots:
            bots[b].append(v)
        else:
            bots[b] = [ v ]

    bot_cmds = dict()
    outputs = dict()

    for c in cmds:
        p = parse("bot {givebot:d} gives low to {lowdest} {lowdestnum:d} and high to {highdest} {highdestnum:d}", c)
        bot_cmds[p["givebot"]] = [ ( p["lowdest"], p["lowdestnum"] ), ( p["highdest"], p["highdestnum"] ) ]

        ld = p["lowdest"]
        hd = p["highdest"]
        ldn = p["lowdestnum"]
        hdn = p["highdestnum"]

        if ld == "output":
            outputs[ldn] = []
        elif ldn not in bots:
            bots[ldn] = []
        if hd == "output":
            outputs[hdn] = []
        elif hdn not in bots:
            bots[hdn] = []
        

    full_bots = bot_holding(bots)
    while full_bots:
        for b in full_bots:

            holdings = sorted(bots[b])
            if holdings[0] == 17 and holdings[1] == 61:
                print "Answer 1:", b
            b_cmd = bot_cmds[b]
            
            ld = b_cmd[0][0]
            hd = b_cmd[1][0]
            ldn = b_cmd[0][1]
            hdn = b_cmd[1][1]

            if ld == "output":
                outputs[ldn].append( holdings[0] )
            else:
                bots[ldn].append( holdings[0] )
            if hd == "output":
                outputs[hdn].append( holdings[1] )
            else:
                bots[hdn].append( holdings[1] )
            del bots[b]
            del bot_cmds[b]
            
        full_bots = bot_holding(bots)
    print "Answer 2:", reduce(mul, outputs[0] + outputs[1] + outputs[2])


if __name__ == "__main__":
    main()
