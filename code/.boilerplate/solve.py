#!/usr/bin/env python
import aocpaiv as aoc


def solve(text):
    xs = aoc.parse_ints(text)
    aoc.trace(xs)
    return sum(map(sum, xs))


def test():
    aoc.test_subject(solve)
    aoc.test('3 2 1') == 6


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
