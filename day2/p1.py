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
            parts = line.split()
            id = int(parts[1][:-1])
            parts = parts[2:]
            rounds = [r.split(',') for r in ' '.join(parts).split(';')]
            possible = True
            bag = { "red": 12, "green": 13, "blue": 14 }
            for round in rounds:
                if not possible:
                    break
                for draw in round:
                    [quantity, color] = draw.split()
                    if bag[color] < int(quantity):
                        possible = False
                        break

            ic(line, possible)
            if (possible):
                sum += id
        print(sum)


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
