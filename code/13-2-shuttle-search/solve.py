#!/usr/bin/env python
import aocpaiv as aoc


def solve(text):
    data = text.strip().splitlines()
    buses = [(int(s), i) for i, s in enumerate(data[1].split(',')) if s != 'x']

    # slow chinese remainder solver, sieve
    buses = sorted(buses, reverse=True)
    m, mt = buses[0]
    t = m - mt
    for x, xt in buses[1:]:
        while (t + xt) % x:
            t += m
        m *= x
    return t


def test():
    aoc.test_subject(solve)
    aoc.test("""
0
17,x,13,19
""") == 3417

    aoc.test("""
0
67,7,59,61
""") == 754018

    aoc.test("""
0
67,x,7,59,61
""") == 779210

    aoc.test("""
0
67,7,x,59,61
""") == 1261476

    aoc.test("""
0
1789,37,47,1889
""") == 1202161486

    aoc.test("""
939
7,13,x,x,59,x,31,19
""") == 1068781


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
