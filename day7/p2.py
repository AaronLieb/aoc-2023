#! /usr/bin/python3
import sys
import itertools
import functools
from icecream import ic
from collections import defaultdict
from collections import Counter


class Soln:
    def __init__(self, inp_file):
        with open(inp_file, "r") as fd:
            self.lines = [x.strip() for x in fd.readlines()]

    def solve(self):
        result = 0
        order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
        hands = [] # (value, bid)
        for line in self.lines:
            [hand, bid] = line.split()
            value = 0
            counter_stuff = Counter(hand)
            counter_stuff['J'] = 0
            c = sorted(list(counter_stuff.items()), key=lambda x: x[1], reverse=True)
            ic(c)
            def j_count():
                return hand.count('J')

            # five of a kind 
            if ((c[0][1]) == 5 - j_count() or j_count() == 5):
                value += (13**19)
            # four of a kind 
            elif ((c[0][1]) == 4 - j_count()):
                value += (13**18)
            # full house 4
            elif ((c[0][1]) == 3 - j_count() and (( c[1][1] == 2 - j_count() and c[0][1] == 3) or c[1][1] == 2) ):
                value += (13**17)
            # 3 of a kind 3
            elif ((c[0][1]) == 3 - j_count()):
                value += (13**16)
            # two pair
            elif ((c[0][1]) == 2 - j_count() and ( ( c[1][1]) == 2 - j_count() and c[0][1] == 2) or c[1][1] == 2 ):
                value += (13**15)
            # pair 2
            elif ((c[0][1]) == 2 - j_count()):
                value += (13**14)
            # high card
            for i in range(0, 5):
                value += (len(order) - order.index(hand[i])) * 13 ** (len(order) - i)

            hands.append((value, int(bid), hand))

            # hand           1       2        3      4        5
            #  v*5^5  +   v*5^4  + v*5^3  + v*5^2 + v*5^1 + v*5^0
        hands = sorted(hands)
        ic(hands)
        for i in range(len(hands)):
            ic(hands[i][1], (i + 1), hands[i][2])
            result += (hands[i][1] * (i + 1))
        print(result)



if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "-d": ic.disable()
    soln = Soln(sys.argv[1] + ".in" if len(sys.argv) > 1 else "small.in")
    soln.solve()
