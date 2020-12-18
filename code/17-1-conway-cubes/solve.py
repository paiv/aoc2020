#!/usr/bin/env python
import aocpaiv as aoc
import io
import itertools


def solve(text, N=6):
    grid = {(0, y, x):1
        for y,s in enumerate(text.strip().splitlines())
        for x,v in enumerate(s)
        if v == '#'}

    def adjacent(k):
        for p in itertools.product((-1, 0, 1), repeat=len(k)):
            if any(p):
                yield tuple(a+b for a, b in zip(k, p))

    assert len(list(adjacent((1,1,1)))) == 26

    def update(k, grid):
        v = grid.get(k)
        occupied = sum(grid.get(q, 0) for q in adjacent(k))
        if occupied == 3:
            return 1
        elif (occupied == 2) and (v == 1):
            return 1
        return 0

    for _ in range(N):
        next = dict()
        ks = {q for k,v in grid.items() if v for q in adjacent(k)}
        for k in ks:
            next[k] = update(k, grid)
        grid = next

    return sum(grid.values())


def dump(grid, z):
    so = io.StringIO()
    print(f'z={z}', file=so)
    qs = {k for k,v in grid.items() if v}
    minx = min(x for z,y,x in qs)
    maxx = max(x for z,y,x in qs)
    miny = min(y for z,y,x in qs)
    maxy = max(y for z,y,x in qs)
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            c = '#' if grid.get((z, y, x)) else '.'
            so.write(c)
        so.write('\n')
    aoc.trace(so.getvalue())


def test():
    aoc.test_subject(solve)
    aoc.test("""
.#.
..#
###
""") == 112


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
