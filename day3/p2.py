#! /usr/bin/python3
import sys
import itertools
import functools
from icecream import ic
from collections import defaultdict


nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

class Soln:
    def __init__(self, inp_file):
        with open(inp_file, "r") as fd:
            self.lines = [x.strip() for x in fd.readlines()]

    def complete_num(self, row, col):
        num = ""
        left = col
        right = col + 1
        while (left >= 0 and self.lines[row][left] in nums):
            num = self.lines[row][left] + num
            left -= 1
        while (right < len(self.lines[row]) and self.lines[row][right] in nums):
            num += self.lines[row][right]
            right += 1
        return (int(num), (row, left))

    def find_nums(self, row, col):
        result = set() 
        clen = len(self.lines[row])
        rlen = len(self.lines)
        if (row > 0 and col > 0 and self.lines[row - 1][col - 1] in nums):
            result.add(self.complete_num(row - 1, col - 1))
        if (row > 0 and self.lines[row - 1][col] in nums):
            result.add(self.complete_num(row - 1, col))
        if (col > 0 and self.lines[row][col - 1] in nums):
            result.add(self.complete_num(row, col - 1))
        if (row < rlen and col < clen and self.lines[row + 1][col + 1] in nums):
            result.add(self.complete_num(row + 1, col + 1))
        if (col < clen and self.lines[row][col + 1] in nums):
            result.add(self.complete_num(row, col + 1))
        if (row < rlen and self.lines[row + 1][col] in nums):
            result.add(self.complete_num(row + 1, col))
        if (row > 0 and col < clen and self.lines[row - 1][col + 1] in nums):
            result.add(self.complete_num(row - 1, col + 1))
        if (row < rlen and col > 0 and self.lines[row + 1][col - 1] in nums):
            result.add(self.complete_num(row + 1, col - 1))
        return result




    def solve(self):
        sum = 0
        for row in range(len(self.lines)):
            line = self.lines[row]
            for col in range(len(line)):
                if line[col] == "*":
                    res = list(self.find_nums(row, col))
                    if len(res) == 2:
                        sum += res[0][0] * res[1][0]
            ic(line)
        print(sum)


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
