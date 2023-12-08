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
        moves = self.lines[0]
        dirs = {}
        for line in self.lines[2:]:
            ic(line)
            parts = line.split()
            [key, _, left, right] = parts
            left = left[1:-1]
            right = right[:-1]
            dirs[key] = (left, right)
            
        curr = 'AAA'
        counter = 0
        while True:
            for move in moves:
                ic(curr, move)
                if (curr == 'ZZZ'):
                    print(counter)
                    return
                if move == 'L':
                    curr = dirs[curr][0]
                else:
                    curr = dirs[curr][1]
                counter += 1






if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
