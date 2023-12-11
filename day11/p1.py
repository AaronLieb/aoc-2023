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

    def find(self, s, ch):
        return [i for i, ltr in enumerate(s) if ltr == ch]

    def solve(self):
        i = 0
        points = []
        while i < len(self.lines):
            line = self.lines[i]
            if line.count('.') == len(line):
                self.lines.insert(i + 1, ',' * len(self.lines[0]))
            i += 1
        new_list = []
        for i in range(len(self.lines[0])):
            # maiking a list with its index element and convert it into string.
            new_string = ''.join([ls[i] for ls in self.lines])
            # appending the new_string int new_list
            new_list.append(new_string)
        self.lines = new_list.copy()
        i = 0
        while i < len(self.lines):
            line = self.lines[i]
            if line.count('.') + line.count(',') == len(line):
                self.lines.insert(i + 1, ',' * len(self.lines[0]))
                i += 1
            x_values = self.find(line, '#')
            points += [(i, x) for x in x_values]
            i += 1
        new_list = []
        for i in range(len(self.lines[0])):
            # maiking a list with its index element and convert it into string.
            new_string = ''.join([ls[i] for ls in self.lines])
            # appending the new_string int new_list
            new_list.append(new_string)
        self.lines = new_list.copy()

        ic(self.lines)

        ic(points)
        result = 0
        multiple = 1000000
        for i in range(len(points)):
            for j in range(i, len(points)):
                for x in range(points[i][0], points[j][0], -1 if points[i][0] > points[j][0] else 1):
                    result += 1
                    if (self.lines[0][x] == ","):
                        result += multiple - 2
                for y in range(points[i][1], points[j][1], -1 if points[i][1] > points[j][1] else 1):
                    result += 1
                    if (self.lines[y][0] == ","):
                        result += multiple - 2
        print(result)


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
