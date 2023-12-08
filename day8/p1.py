#! /usr/bin/python3
import sys
import itertools
from functools import lru_cache
from icecream import ic
from collections import defaultdict


class Soln:
    def __init__(self, inp_file):
        with open(inp_file, "r") as fd:
            self.lines = [x.strip() for x in fd.readlines()]


    def solve(self):
        moves = self.lines[0]
        dirs = {}
        currs = []
        for line in self.lines[2:]:
            ic(line)
            parts = line.split()
            [key, _, left, right] = parts
            left = left[1:-1]
            right = right[:-1]
            dirs[key] = (left, right)
            if (key[-1] == 'A'):
                currs.append(key)
            
        
        counter = 0
        history = []
        past_z = {}
        while True:
            for move in moves:
                # ic(currs, move)
                history.append(currs.copy())
                z_sum = 0
                for i in range(len(currs)):
                    if currs[i][-1] == 'Z':
                        if (i not in past_z):
                            past_z[i] = [counter]
                        else:
                            past_z[i].append(counter - past_z[i][-1])
                        z_sum += 1

                ic(len(currs))
                # ic(past_z)
                if sum([1 for curr in currs if curr[-1] == 'Z']) == len(currs):
                    print(counter)
                    return
                if move == 'L':
                    for i in range(len(currs)):
                        currs[i] = dirs[currs[i]][0]
                else:
                    for i in range(len(currs)):
                        currs[i] = dirs[currs[i]][1]
                counter += 1

#              0: [14893, 14893, 29786, 29786, 44679],
#              1: [19951, 19951, 39902, 39902],
#              2: [22199, 22199, 44398],
#              3: [16579, 16579, 33158, 33158, 49737],
#              4: [17141, 17141, 34282, 34282],
#              5: [12083, 12083, 24166, 24166, 36249, 36249, 48332]}




if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
