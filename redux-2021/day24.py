#!/usr/bin/env python
import re


def part1(data):
    moves = {'e':1, 'se':1j, 'sw':-1+1j, 'w':-1, 'nw':-1j, 'ne':1-1j}
    grid = dict()
    for s in data.splitlines():
        pos = 0
        for op in re.findall(r'e|se|sw|w|nw|ne', s):
            pos += moves[op]
        grid[pos] = 1 - grid.get(pos, 0)
    return sum(grid.values())


def dump(grid):
    print()
    print(sum(grid.values()))
    sq = {(int(k.imag),(2 * int(k.real) + (int(k.imag) & ~1))):v for k,v in grid.items()}
    dx = min(x for y,x in sq)
    dy = min(y for y,x in sq)
    w = max(x for y,x in sq) - dx + 1
    h = max(y for y,x in sq) - dy + 1
    for y in range(h):
        if y & 1:
            print(' ', end='')
        for x in range(0, w, 2):
            q = sq.get((y+dy,x+dx), 0)
            print('.#'[q], end=' ')
        print()


def part2(data, N=100):
    moves = {'e':1, 'se':1j, 'sw':-1+1j, 'w':-1, 'nw':-1j, 'ne':1-1j}
    grid = dict()
    for s in data.splitlines():
        pos = 0
        for op in re.findall(r'e|se|sw|w|nw|ne', s):
            pos += moves[op]
        grid[pos] = 1 - grid.get(pos, 0)

    for _ in range(N):
        soon = dict()
        pois = set((k + i) for k,v in grid.items() if v for i in moves.values())
        for p in pois:
            n = sum(grid.get(p+i, 0) for i in moves.values())
            if grid.get(p, 0):
                if (n == 0) or (n > 2):
                    soon[p] = 0
                else:
                    soon[p] = 1
            else:
                if n == 2:
                    soon[p] = 1
        grid = soon

    return sum(grid.values())


data = '''
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
'''.strip()
assert part1(data) == 10
assert part2(data) == 2208


data = open('day24.in').read()
print(part1(data))
print(part2(data))