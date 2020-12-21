#!/usr/bin/env python
import aocpaiv as aoc
import re
from collections import Counter


def solve(text):
    sides = Counter()
    tiles = dict()
    for s in text.strip().split('\n\n'):
        h, *xs = s.strip().splitlines()
        n = int(re.findall(r'\d+', h)[0])
        xs = tuple(tuple(int(x == '#') for x in row) for row in xs)
        top, bottom = xs[0], xs[-1]
        left = tuple(row[0] for row in xs)
        right = tuple(row[-1] for row in xs)
        sig = [
            min(packbits(top), packbits(top[::-1])),
            min(packbits(right), packbits(right[::-1])),
            min(packbits(bottom), packbits(bottom[::-1])),
            min(packbits(left), packbits(left[::-1])),
        ]
        sides.update(sig)
        tiles[n] = sig

    res = 1
    for n, sig in tiles.items():
        if sum(sides[x] for x in sig) == 6:
            res *= n
    return res


def packbits(xs):
    w = len(xs)-1
    return sum((x << (w-i)) for i,x in enumerate(xs))


def test():
    aoc.test_subject(solve)
    aoc.test("""
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
""") == 20899048083289


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
