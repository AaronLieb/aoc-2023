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
        result = 0
        for line in self.lines:
            ic(line)
            nums = [int(x) for x in line.split()]
            hist = [nums]
            while hist[-1].count(0) != len(hist[-1]):
                next = []
                for i in range(len(hist[-1]) - 1):
                    next.append(hist[-1][i + 1] - hist[-1][i])
                hist.append(next)
            hist = hist[::-1]
            hist[0].insert(0, 0)
            for i in range(1, len(hist)):
                first = hist[i][0] - hist[i - 1][0] 
                hist[i].insert(0, first)
                if (i == len(hist) - 1):
                    result += first
                ic(first)
            ic(hist)
        print(result)




if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
