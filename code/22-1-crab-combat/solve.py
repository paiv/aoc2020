#!/usr/bin/env python
import aocpaiv as aoc
import re
from collections import deque


def solve(text):
    p1, p2 = text.strip().split('\n\n')
    p1 = list(map(int, re.findall(r'^(\d+)', p1, re.M)))
    p2 = list(map(int, re.findall(r'^(\d+)', p2, re.M)))

    p1, p2 = map(deque, (p1, p2))
    while p1 and p2:
        x, y = p1.popleft(), p2.popleft()
        if x > y:
            p1.append(x)
            p1.append(y)
        else:
            p2.append(y)
            p2.append(x)

    return sum((x * i) for i,x in enumerate(reversed(p1 or p2), 1))


def test():
    aoc.test_subject(solve)
    aoc.test("""
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
""") == 306


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
