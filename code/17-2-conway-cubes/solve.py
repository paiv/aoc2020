#!/usr/bin/env python
import aocpaiv as aoc


def solve(text, N=6):
    grid = {(0, 0, y, x):1
        for y,s in enumerate(text.strip().splitlines())
        for x,v in enumerate(s)
        if v == '#'}

    def adjacent(k):
        w, z, y, x = k
        for dw in range(-1, 2):
            for dz in range(-1, 2):
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if not (dx == 0 and dy == 0 and dz == 0 and dw == 0):
                            yield (w + dw, z + dz, y + dy, x + dx)

    assert len(list(adjacent((1,1,1,1)))) == 80

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


def test():
    aoc.test_subject(solve)
    aoc.test("""
.#.
..#
###
""") == 848


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
