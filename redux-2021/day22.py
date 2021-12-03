#!/usr/bin/env python
import re
from collections import deque
from itertools import islice


def part1(data):
    pa, pb = data.split('\n\n')
    pa = deque(map(int, re.findall(r'^\d+', pa, re.M)))
    pb = deque(map(int, re.findall(r'^\d+', pb, re.M)))

    while pa and pb:
        x,y = pa.popleft(), pb.popleft()
        if x > y:
            pa.append(x)
            pa.append(y)
        else:
            pb.append(y)
            pb.append(x)

    ans = sum((x * i) for i,x in enumerate(reversed(pa or pb), 1))
    return ans


def part2(data):
    pa, pb = data.split('\n\n')
    pa = deque(map(int, re.findall(r'^\d+', pa, re.M)))
    pb = deque(map(int, re.findall(r'^\d+', pb, re.M)))

    def subgame(deck1, deck2):
        seen = set()
        while deck1 and deck2:
            k = (tuple(deck1), tuple(deck2))
            if k in seen: return 1
            seen.add(k)

            x,y = deck1.popleft(), deck2.popleft()

            if (x <= len(deck1)) and (y <= len(deck2)):
                win1 = subgame(deque(islice(deck1, x)), deque(islice(deck2, y)))
            else:
                win1 = x > y

            if win1:
                deck1.append(x)
                deck1.append(y)
            else:
                deck2.append(y)
                deck2.append(x)

        return len(deck1) > 0

    subgame(pa, pb)

    ans = sum((x * i) for i,x in enumerate(reversed(pa or pb), 1))
    return ans


data = '''
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
'''.strip()
assert part1(data) == 306
assert part2(data) == 291


data = '''
Player 1:
43
19

Player 2:
2
29
14
'''
assert part2(data) == 105


data = open('day22.in').read()
print(part1(data))
print(part2(data))