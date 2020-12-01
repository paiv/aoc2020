#!/usr/bin/env python
import aocpaiv as aoc


def solve(text, N=2020):
    xs = aoc.parse_ints_flatten(text)
    aoc.trace(xs)
    for i, x in enumerate(xs):
        for y in xs[i+1:]:
            if x + y == N:
                return x * y


def test():
    aoc.test_subject(solve)
    aoc.test('''
1721
979
366
299
675
1456
    ''') == 514579


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
