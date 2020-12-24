#!/usr/bin/env python
import aocpaiv as aoc
import re


def solve(text):
    moves = ({'w':-1, 'e':1, 'nw':-1j, 'ne':1-1j, 'sw':1j, 'se':1+1j},
        {'w':-1, 'e':1, 'nw':-1-1j, 'ne':-1j, 'sw':-1+1j, 'se':1j})

    grid = dict()
    for line in text.strip().splitlines():
        p = 0
        for op in re.findall(r'se|sw|ne|nw|e|w', line):
            p += moves[int(p.imag) % 2][op]
        grid[p] = 1 - grid.get(p, 0)
    return sum(grid.values())


def test():
    aoc.test_subject(solve)
    aoc.test('nwwswee') == 1
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
""") == 10


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
