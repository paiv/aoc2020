#!/usr/bin/env python -OO
import aocpaiv as aoc


def solve(text, G=7):
    p1, p2 = map(int, text.strip().split())

    def xmas(x, N):
        return pow(x, N, 20201227)

    def getloop(x, p):
        for i in range(10 ** 10):
            if p == xmas(x, i):
                return i

    x = getloop(G, p1)
    aoc.trace(x)
    y = getloop(G, p2)
    aoc.trace(y)
    return xmas(xmas(G, y), x)


def test():
    aoc.test_subject(solve)

    aoc.test("""
5764801
17807724
""") == 14897079


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
