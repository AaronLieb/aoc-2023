#! /usr/bin/python3
import sys
import itertools
from functools import cache
from icecream import ic
from collections import defaultdict


class Soln:
    def __init__(self, inp_file):
        with open(inp_file, "r") as fd:
            self.lines = [x.strip() for x in fd.readlines()]


    @cache
    def score(self, row):
        line = self.lines[row]
        card = [set(side.split()) for side in line.split(':')[1].split('|')]
        matches = len(set.intersection(card[0], card[1]))
        return matches + sum([self.score(i) for i in range(row + 1, row + matches + 1)])


    def solve(self):
        print(len(self.lines) + sum([self.score(i) for i in range(len(self.lines))]))


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
