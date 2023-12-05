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
        seed_p = [int(x) for x in self.lines[0].split()[1:]]
        seeds = []
        for i in range(0, len(seed_p), 2):
            seeds.append((seed_p[i], seed_p[i + 1]))
        next = []

        ic(seeds)

        for line in self.lines[2:]:
            ic(line)
            if len(line) == 0:
                next += seeds
                seeds = next.copy()
                ic(seeds)
                next = []
            elif '-' in line:
                continue
            else:
                [dst, src, rng] = [int(x) for x in line.split()]
                to_remove = []
                for seed in seeds:
                    # ic(seed, src, dst, rng)
                    # oooo
                    #   xxxxx
                    if seed[0] < src and (seed[0] + seed[1] - 1) in range(src, src + rng):
                        left = src - seed[0]
                        right = seed[1] - left
                        ic("1", seed[0], dst)
                        next.append( (seed[0], left) )
                        next.append( (dst, right) )

                        to_remove.append(seed)
                    #   oo
                    # xxxxx
                    elif seed[0] in range(src, src + rng) and seed[0] + seed[1] - 1 in range(src, src + rng):
                        ic("2", seed[0], dst)
                        next.append((dst + seed[0] - src, seed[1]))
                        to_remove.append(seed)
                    #     ooo
                    # xxxxx
                    elif seed[0] in range(src, src  + rng) and seed[0] + seed[1] > src + rng:
                        left = (src + rng) - seed[0]
                        right = seed[1] - left
                        ic("3", seed[0], dst)
                        next.append((dst + seed[0] - src, left))
                        next.append((src + rng, right))
                        to_remove.append(seed)
                    # oooooooo
                    #  xxxxx  
                    elif seed[0] < src and seed[0] + seed[1] > src + rng:
                        left = src - seed[0]
                        right = seed[1] - left - rng
                        ic("4", seed[0], dst)
                        next.append((seed[0], left))
                        next.append((dst, rng))
                        next.append((src + rng, right))
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
