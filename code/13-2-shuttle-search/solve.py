#!/usr/bin/env python
import aocpaiv as aoc


def solve(text):
    data = text.strip().splitlines()
    buses = [(int(s), i) for i, s in enumerate(data[1].split(',')) if s != 'x']
    buses = sorted(buses, reverse=True)

    # slow chinese remainder solver
    def sieve(off, t, m):
        if off >= len(buses):
            return t
        x, xt = buses[off]
        while (t + xt) % x:
            t += m
        return sieve(off + 1, t, m * x)

    m, mt = buses[0]
    return sieve(1, m - mt, m)


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
