import sys
import itertools
import functools
from icecream import ic
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self._get_node(word)
        return node is not None and node.is_end_of_word

    def starts_with(self, prefix):
        return self._get_node(prefix) is not None

    def _get_node(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

class Soln:
    def __init__(self, inp_file):
        with open(inp_file, "r") as fd:
            self.lines = [x.strip() for x in fd.readlines()]

    def solve(self):
        sum = 0
        debug_sum = ""
        pt = Trie()
        pt_rev = Trie()
        words = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        word_to_num = {
                'one': 1,
                'two': 2,
                'three': 3,
                'four': 4,
                'five': 5,
                'six': 6,
                'seven': 7,
                'eight': 8,
                'nine': 9,
                }
        for word in words:
            pt.insert(word)
        for word in words:
            pt_rev.insert(word[::-1])

        for line in self.lines:
            num = 0
            found = False
            for i in range(len(line)):
                if (found):
                    break
                word = ""
                for j in range(i, len(line)):
                    word += line[j]
                    if (pt.search(word)):
                        if (len(word) > 1):
                            num += 10 * word_to_num[word]
                        else:
                            num += 10 * int(word)
                        found = True
                        break
                    elif not pt.starts_with(word):
                        break

            line = line[::-1]
            found = False
            for i in range(len(line)):
                if (found):
                    break
                word = ""
                for j in range(i, len(line)):
                    word += line[j]
                    if (pt_rev.search(word)):
                        if (len(word) > 1):
                            num += word_to_num[word[::-1]]
                        else:
                            num += int(word)
                        found = True
                        break
                    elif not pt_rev.starts_with(word):
                        break

            sum += num
            line = line[::-1]
            ic(line, num)
        print(sum)



if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
