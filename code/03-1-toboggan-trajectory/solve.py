#!/usr/bin/env python
import aocpaiv as aoc


def solve(text):
    grid = text.strip().splitlines()
    total = 0
    for y, row in enumerate(grid):
        total += row[y * 3 % len(row)] == '#'
    return total


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
""") == 7


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
