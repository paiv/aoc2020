#!/usr/bin/env python
import aocpaiv as aoc


def solve(text):
    grid = text.strip().splitlines()
    res = 1
    for dy, dx in [(1,1), (1,3), (1,5), (1,7), (2,1)]:
        total = 0
        for y, row in enumerate(grid[::dy]):
            total += row[y * dx % len(row)] == '#'
        res *= total
    return res


def test():
    aoc.test_subject(solve)
    aoc.test("""
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""") == 336


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
