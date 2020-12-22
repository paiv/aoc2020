#!/usr/bin/env python
import aocpaiv as aoc
import re
from collections import deque


def solve(text):
    p1, p2 = text.strip().split('\n\n')
    p1 = tuple(map(int, re.findall(r'^(\d+)', p1, re.M)))
    p2 = tuple(map(int, re.findall(r'^(\d+)', p2, re.M)))
    score = None

    def subgame(p1, p2, nest=0):
        p1, p2 = map(deque, (p1, p2))
        seen = set()
        while p1 and p2:
            k = (tuple(p1), tuple(p2))
            if k in seen: break
            seen.add(k)

            x, y = p1.popleft(), p2.popleft()
            if x <= len(p1) and y <= len(p2):
                t1 = tuple(p1)[:x]
                t2 = tuple(p2)[:y]
                win = subgame(t1, t2, nest+1)
            else:
                win = 1 if (x > y) else 2

            if win == 1:
                p1.append(x)
                p1.append(y)
            else:
                p2.append(y)
                p2.append(x)

        if nest == 0:
            nonlocal score
            score = sum((x * i) for i,x in enumerate(reversed(p1 or p2), 1))
        return 1 if p1 else 2

    subgame(p1, p2)
    return score


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
""") == 291


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
