#!/usr/bin/env python
import aocpaiv as aoc
import io
import math
import re
from collections import namedtuple


Tile = namedtuple('Tile', 'n xs')
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
        return n, Tile(n, xs)
    tiles = dict(parse(s) for s in text.strip().split('\n\n'))

    def top(tile): return tile.xs[0]
    def bottom(tile): return tile.xs[-1]
    def left(tile): return tuple(row[0] for row in tile.xs)
    def right(tile): return tuple(row[-1] for row in tile.xs)

    def drot(tile):
        return Tile(tile.n, tuple(zip(*tile.xs)))
    def flipy(tile):
        return Tile(tile.n, tile.xs[::-1])
    def flipx(tile):
        return Tile(tile.n, tuple(row[::-1] for row in tile.xs))
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
    def nth(tile, n):
        return transops[n](tile)

    def fitstl(t, N, W):
        if N and top(t) != bottom(N): return False
        if W and left(t) != right(W): return False
        return True

    def search_arrangement():
        ntiles = set(tiles.keys())
        side = int(math.sqrt(len(ntiles)))

        def qry(n, ti):
            return nth(tiles[n], ti)
        def fits(path, t):
            idx = len(path)
            y, x = divmod(idx, side)
            left = qry(*path[y*side+(x-1)]) if x > 0 else None
            top = qry(*path[(y-1)*side+x]) if y > 0 else None
            return fitstl(t, top, left)

        fringe = [[]]
        while fringe:
            path = fringe.pop()
            if len(path) == len(ntiles):
                aoc.trace('found', path)
                ts = [nth(tiles[n], ti) for n,ti in path]
                return [[ts[y*side+x] for x in range(side)] for y in range(side)]
            for n in (ntiles - {n for n,_ in path}):
                for ti, t in enumerate(transforms(tiles[n])):
                    if fits(path, t):
                        fringe.append(path + [(n,ti)])

    m = search_arrangement()

    def pack_image(grid):
        side = len(grid)
        tile_size = len(grid[0][0].xs) - 2
        pxside = side * tile_size
        def pix(px, py):
            gy, y = divmod(py, tile_size)
            gx, x = divmod(px, tile_size)
            t = grid[gy][gx]
            return t.xs[y+1][x+1]
        return [[pix(px, py) for px in range(pxside)] for py in range(pxside)]

    pic = pack_image(m)

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

    for t in transforms(Tile(0, pic)):
        monsters = set(find_monsters(t.xs))
        if monsters:
            aoc.trace(ink(pic, monsters))
            return sum(x for row in t.xs for x in row) - len(monsters) * len(monster)


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
