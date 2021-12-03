#!/usr/bin/env python
import itertools
import re
from collections import Counter, defaultdict
from functools import reduce
from dataclasses import dataclass


def part1(data):
    def tilep(s):
        tid, = re.findall(r'\d+', s)
        tile = re.findall(r'^[#.]+$', s, re.M)
        tilet = list(zip(*tile))
        sides = {sum((1 << i) for i,c in enumerate(q) if c == '#')
            for s in [tile[0], tile[-1], tilet[0], tilet[-1]] for q in [s, s[::-1]]}
        return (int(tid), sides)
    tiles = [tilep(s) for s in data.strip().split('\n\n')]
    for (_, xs), (_, ys) in itertools.combinations(tiles, 2):
        t = xs & ys
        xs -= t
        ys -= t
    ans = reduce(int.__mul__, (t for t, xs in tiles if len(xs) == 4))
    return ans


def part2(data):
    @dataclass
    class Tile:
        tid: int
        sides: list[int]
        body: list[str]

    byside = defaultdict(set)
    refl = dict()
    def tilep(s):
        tid, = map(int, re.findall(r'\d+', s))
        tile = re.findall(r'^[#.]+$', s, re.M)
        body = tuple(s[1:-1] for s in tile[1:-1])
        tilet = list(zip(*tile))
        sides = list()
        for s in [tile[0], tile[-1], tilet[0], tilet[-1]]:
            t = sum((1 << i) for i,c in enumerate(s) if c == '#')
            sides.append(t)
            byside[t].add(tid)
            q = sum((1 << i) for i,c in enumerate(s[::-1]) if c == '#')
            byside[q].add(tid)
            refl[t] = q
            refl[q] = t
        return (tid, Tile(tid, sides, body))
    tiles = dict(tilep(s) for s in data.strip().split('\n\n'))

    def rotate(tile):
        t, b, l, r = tile.sides
        tile.sides = (refl[l], refl[r], b, t)
        tile.body = [''.join(s[::-1]) for s in zip(*tile.body)]

    def flip(tile):
        t, b, l, r = tile.sides
        tile.sides = (refl[t], refl[b], r, l)
        tile.body = [s[::-1] for s in tile.body]

    def adjust(tile, sid, v):
        for _ in range(2):
            for _ in range(4):
                if tile.sides[sid] == v:
                    return
                rotate(tile)
            flip(tile)

    corner = Counter(x for xs in byside.values() if len(xs) == 1 for x in xs).most_common(1)[0][0]

    sea = list()
    start = next((corner, s) for s in tiles[corner].sides if len(byside[s]) == 1)
    seen = set()
    while start:
        run = list()
        sea.append(run)

        tid, sid = start
        start = None
        seen.add(tid)
        adjust(tiles[tid], 0, sid)

        if len(byside[tiles[tid].sides[3]]) == 1:
            flip(tiles[tid])

        bottom = tiles[tid].sides[1]
        for t in byside[bottom]:
            if t not in seen:
                start = (t, bottom)

        left = tid
        while left:
            tid, left = left, None
            run.append(tiles[tid].body)
            right = tiles[tid].sides[3]
            for t in byside[right]:
                if t not in seen:
                    seen.add(t)
                    adjust(tiles[t], 2, right)
                    left = t

    sea = [''.join(c[i] for c in run) for run in sea for i in range(len(run[0]))]
    # print('\n'.join(sea))

    monster = '''
..................#.
#....##....##....###
.#..#..#..#..#..#...
'''.strip().splitlines()

    def coast(sea):
        monsters = 0
        for y in range(len(monster)-1, len(sea)):
            for p in range(len(sea[y]) - len(monster[0]) + 1):
                monsters += all((b == '.' or a == b) for j,m in enumerate(monster[::-1]) for a,b in zip(sea[y-j][p:], m))
        return monsters

    def rotate(xs): return [''.join(s[::-1]) for s in zip(*xs)]
    def flip(xs): return [s[::-1] for s in xs]

    for op in (rotate, rotate, rotate, rotate, flip, rotate, rotate, rotate, rotate):
        if (monsters := coast(sea)): break
        sea = op(sea)

    water = sum(s.count('#') for s in sea)
    m = sum(s.count('#') for s in monster)
    ans = water - monsters * m
    # print(ans, (water, monsters))
    return ans


data = '''
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
'''.strip()
assert part1(data) == 20899048083289
assert part2(data) == 273


# data = open('day20.in').read()
data = open('../code/20-2-jurassic-jigsaw/input.txt').read()
print(part1(data))
print(part2(data))