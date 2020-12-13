#!/usr/bin/env python
import aocpaiv as aoc


def solve(text):
    data = text.strip().splitlines()
    T = int(data[0])
    buses = [int(s) for s in data[1].split(',') if s != 'x']

    t, bus = min(((T + m - 1) // m * m, m) for m in buses)
    return (t - T) * bus


def test():
    aoc.test_subject(solve)
    aoc.test("""
939
7,13,x,x,59,x,31,19
""") == 295


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
