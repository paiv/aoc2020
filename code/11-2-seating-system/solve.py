#!/usr/bin/env python
import aocpaiv as aoc
from collections import defaultdict


def solve(text):
    VACANT, OCCUPIED = 1, 2

    grid = {(y, x):VACANT
        for y,s in enumerate(text.strip().splitlines())
        for x,v in enumerate(s)
        if v == 'L'}
    w = max(x for _,x in grid.keys()) + 1
    h = max(y for y,_ in grid.keys()) + 1

    adj = defaultdict(set)
    for y, x in grid.keys():
        for dy, dx in zip((-1, -1, -1, 0, 0, 1, 1, 1), (-1, 0, 1, -1, 1, -1, 0, 1)):
            ay, ax = dy, dx
            while (0 <= y + ay < h) and (0 <= x + ax < w):
                q = (y + ay, x + ax)
                if grid.get(q):
                    adj[(y, x)].add(q)
                    adj[q].add((y, x))
                    break
                ay += dy
                ax += dx

    def update(k, v, grid):
        occupied = sum(grid[q] == OCCUPIED for q in adj[k])
        if (v == VACANT) and (occupied == 0):
            return OCCUPIED
        elif (v == OCCUPIED) and (occupied >= 5):
            return VACANT
        return v

    prev = None
    state = tuple()
    while state != prev:
        grid = {k:update(k, v, grid) for k, v in grid.items()}
        prev = state
        state = tuple(sorted(grid.items()))

    return sum(x == OCCUPIED for x in grid.values())


def test():
    aoc.test_subject(solve)
    aoc.test("""
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""") == 26


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
