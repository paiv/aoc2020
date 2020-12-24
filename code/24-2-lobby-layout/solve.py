#!/usr/bin/env python
import aocpaiv as aoc
import re


def solve(text, N=100):
    moves = {'w':-1, 'e':1, 'nw':-1j, 'ne':1-1j, 'sw':-1+1j, 'se':1j}

    grid = dict()
    for line in text.strip().splitlines():
        p = 0
        for op in re.findall(r'se|sw|ne|nw|e|w', line):
            p += moves[op]
        grid[p] = 1 - grid.get(p, 0)

    def adjacent(p):
        for x in moves.values():
            yield p + x

    def update(grid):
        def nb(p):
            return sum(grid.get(i,0) for i in adjacent(p))
        def rulex(v, n):
            if (v == 1) and ((n == 0) or (n > 2)): return 0
            if (v == 0) and (n == 2): return 1
            return v
        next = dict()
        xs = set(q for p,v in grid.items() if v for q in adjacent(p))
        for p in xs:
            next[p] = rulex(grid.get(p,0), nb(p))
        return next

    for day in range(N):
        grid = update(grid)

    return sum(grid.values())



def test():
    aoc.test_subject(solve)
    aoc.test("""
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
""") == 2208


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
