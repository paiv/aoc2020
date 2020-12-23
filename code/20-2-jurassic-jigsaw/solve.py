#!/usr/bin/env python
import aocpaiv as aoc
import io
import math
import re
from collections import defaultdict, namedtuple


Tile = namedtuple('Tile', 'n xs sig')

Monster = """
..................#.
#....##....##....###
.#..#..#..#..#..#...
"""
monster = {(y,x):1
    for y,row in enumerate(Monster.strip().splitlines())
    for x,c in enumerate(row) if c == '#'}


def solve(text):
    def parse(s):
        h, *xs = s.strip().splitlines()
        n = int(re.findall(r'\d+', h)[0])
        xs = tuple(tuple(int(x == '#') for x in row) for row in xs)
        top, bottom = xs[0], xs[-1]
        left = tuple(row[0] for row in xs)
        right = tuple(row[-1] for row in xs)
        sig = (
            min(packbits(top), packbits(top[::-1])),
            min(packbits(right), packbits(right[::-1])),
            min(packbits(bottom), packbits(bottom[::-1])),
            min(packbits(left), packbits(left[::-1])),
        )
        return n, Tile(n, xs, sig)
    tiles = dict(parse(s) for s in text.strip().split('\n\n'))

    edges = defaultdict(set)
    for tile in tiles.values():
        for s in tile.sig:
            edges[s].add(tile.n)

    side = int(math.sqrt(len(tiles)))
    grid = [[[None, None] for x in range(side)] for y in range(side)]
    orient = [[[None, None] for x in range(side)] for y in range(side)]
    corner = next(t for n, t in tiles.items() if sum(len(edges[x]) for x in t.sig) == 6)
    grid[0][0] = corner.n
    down, right = set(), set()
    y, x = [s for s in corner.sig if len(edges[s]) > 1]
    down.add(y)
    right.add(x)
    orient[0][0] = (None, x, y, None)
    for y in range(side):
        for x in range(side):
            if x > 0:
                t = tiles[grid[y][x-1]]
                q, s = next((tiles[q],s) for s in t.sig if s in right for q in edges[s] if q != t.n)
                grid[y][x] = q.n
                i = q.sig.index(s)
                r = q.sig[(i+2)%4]
                d = q.sig[(i+1)%4]
                if d in down:
                    u = d
                    down.remove(u)
                    d = q.sig[(i+3)%4]
                elif len(edges[d]) == 1:
                    u = d
                    d = q.sig[(i+3)%4]
                else:
                    u = q.sig[(i+3)%4]
                    down.discard(u)
                ox = (u, r, d, s)
                right.remove(s)
                right.add(r)
                down.add(d)
                orient[y][x] = ox
            elif y > 0:
                t = tiles[grid[y-1][x]]
                q, s = next((tiles[q],s) for s in t.sig if s in down for q in edges[s] if q != t.n)
                grid[y][x] = q.n
                i = q.sig.index(s)
                d = q.sig[(i+2)%4]
                r = q.sig[(i+1)%4]
                if r in right:
                    l = r
                    right.remove(l)
                    r = q.sig[(i+3)%4]
                elif len(edges[r]) == 1:
                    l = r
                    r = q.sig[(i+3)%4]
                else:
                    l = q.sig[(i+3)%4]
                    right.discard(l)
                ox = (s, r, d, l)
                down.remove(s)
                down.add(d)
                right.add(r)
                orient[y][x] = ox

    def drot(tile):
        return Tile(tile.n, tuple(zip(*tile.xs)), tile.sig[::-1])
    def flipy(tile):
        sig = (tile.sig[2], tile.sig[1], tile.sig[0], tile.sig[3])
        return Tile(tile.n, tile.xs[::-1], sig)
    def rot(tile):
        return flipy(drot(tile))

    transops = [
        lambda tile: tile,
        lambda tile: rot(tile),
        lambda tile: rot(rot(tile)),
        lambda tile: rot(rot(rot(tile))),
        lambda tile: flipy(tile),
        lambda tile: rot(flipy(tile)),
        lambda tile: rot(rot(flipy(tile))),
        lambda tile: rot(rot(rot(flipy(tile)))),
    ]
    def transforms(tile):
        for op in transops: yield op(tile)

    def pack_image(grid, orient):
        side = len(grid)
        tile_size = len(tiles[grid[0][0]].xs) - 2
        pxside = side * tile_size
        def pix(px, py):
            gy, y = divmod(py, tile_size)
            gx, x = divmod(px, tile_size)
            n = grid[gy][gx]
            ox = orient[gy][gx]
            t = tiles[n]
            for q in transforms(t):
                if q.sig[1:3] == ox[1:3]:
                    return q.xs[y+1][x+1]
        return [[pix(px, py) for px in range(pxside)] for py in range(pxside)]

    pic = pack_image(grid, orient)

    def find_monsters(pic):
        mw = max(x for y,x in monster) + 1
        mh = max(y for y,x in monster) + 1
        pxside = len(pic)
        for y in range(pxside - mh + 1):
            for x in range(pxside - mw + 1):
                if all(pic[y+dy][x+dx] for dy,dx in monster):
                    yield (y, x)

    def count_monsters(pic):
        return sum(1 for _ in find_monsters(pic))

    for t in transforms(Tile(0, pic, sig=(0,0,0,0))):
        monsters = set(find_monsters(t.xs))
        if monsters:
            aoc.trace(ink(pic, monsters))
            return sum(x for row in t.xs for x in row) - len(monsters) * len(monster)


def packbits(xs):
    w = len(xs)-1
    return sum((x << (w-i)) for i,x in enumerate(xs))


def ink(pic, monsters=None):
    mps = {(oy+y, ox+x) for oy,ox in (monsters or set()) for y,x in monster}
    so = io.StringIO()
    for y,row in enumerate(pic):
        for x,c in enumerate(row):
            c = 'O' if (y,x) in mps else '.#'[c]
            so.write(c)
        so.write('\n')
    return so.getvalue()[:-1]


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
""") == 273


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
