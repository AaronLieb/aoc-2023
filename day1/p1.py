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
            nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            num = ''.join(c for c in line if c in nums)
            num = int(num[0] + num[-1])
            ic(line, num)
            sum += num
        print(sum)



if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
