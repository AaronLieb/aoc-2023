#! /usr/bin/python3
import sys
import random
import itertools
import functools
from icecream import ic
from collections import defaultdict


class Soln:
    def __init__(self, inp_file):
        with open(inp_file, "r") as fd:
            self.lines = [x.strip() for x in fd.readlines()]

    def solve(self):
        seed_p = [int(x) for x in self.lines[0].split()[1:]]
        ranges = []
        seeds = set()
        for i in range(0, len(seed_p), 2):
            start = seed_p[i]
            rng = seed_p[i + 1]
            ranges.append((start, rng))
        print(ranges.index((961540761, 489996751)))
        for i in range(0, 10_000):
            # rdi = random.randint(0, len(ranges) - 1)
            rdi = 4
            seed = random.randint(1_392_040_000, 1_392_050_000)
            entry = (seed, (seed, ranges[rdi]))
            seeds.add(entry)
        seeds = list(seeds)

        next = []
        for line in self.lines[2:]:
            ic(line)
            if len(line) == 0:
                next += seeds
                seeds = next.copy()
                next = []
            elif '-' in line:
                continue
            else:
                [dst, src, rng] = [int(x) for x in line.split()]
                to_remove = []
                for seed in seeds:
                    if seed[0] in range(src, src + rng):
                        next.append((dst + abs(seed[0] - src), seed[1]))
                        to_remove.append(seed)
                for r in to_remove:
                    seeds.remove(r)

        next += seeds
        seeds = next.copy()
        next = []
        # ic(seeds)
        print(min(seeds))


                





if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
