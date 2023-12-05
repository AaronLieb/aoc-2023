#! /usr/bin/python3
import sys
import itertools
import functools
from icecream import ic
from collections import defaultdict


class Soln:
    def __init__(self, inp_file):
        with open(inp_file, "r") as fd:
            self.lines = [x.strip() for x in fd.readlines()]

    def solve(self):
        sum = 0
        for line in self.lines:
            card = [set(side.split()) for side in line.split(':')[1].split('|')]
            matches = len(set.intersection(card[0], card[1]))
            if (matches > 0):
                sum += 2**(matches - 1)
            ic(card, 2**(matches - 1))
        print(sum)


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
