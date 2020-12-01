#!/usr/bin/env python -OO
import aocpaiv as aoc


def solve(text, N=2020):
    xs = aoc.parse_ints_flatten(text)
    aoc.trace(xs)
    for i, x in enumerate(xs):
        for j, y in enumerate(xs[i+1:]):
            for z in xs[i+j+2:]:
                if x + y + z == N:
                    return x * y * z

def test():
    aoc.test_subject(solve)
    aoc.test('''
1721
979
366
299
675
1456
    ''') == 241861950


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
