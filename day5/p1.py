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
        seeds = [int(x) for x in self.lines[0].split()[1:]]
        next = []
        for line in self.lines[2:]:
            ic(line)
            if len(line) == 0:
                next += seeds
                seeds = next.copy()
                ic(next)
                next = []
            elif '-' in line:
                continue
            else:
                [dst, src, rng] = [int(x) for x in line.split()]
                to_remove = []
                for seed in seeds:
                    ic(seed, src, dst, rng)
                    if seed in range(src, src + rng):
                        ic("in range")
                        next.append(dst + abs(seed - src))
                        to_remove.append(seed)
                for r in to_remove:
                    seeds.remove(r)

        next += seeds
        seeds = next.copy()
        next = []
        ic(seeds)
        print(min(seeds))


                





if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
