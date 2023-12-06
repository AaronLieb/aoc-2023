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
        times = [int(x) for x in self.lines[0].split()[1:]]
        dists = [int(x) for x in self.lines[1].split()[1:]]
        result = 1
        for i in range(len(times)):
            p_sum = 0
            for t in range(1, times[i]):
                d = t * (times[i] - t)
                if d > dists[i]:
                    p_sum += 1
            result *= p_sum
        print(result)



if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
