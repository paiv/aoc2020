#!/usr/bin/env python -OO
import aocpaiv as aoc
import re


def solve(text):
    total = 0
    for x, y, c, p in re.findall(r'(\d+)\-(\d+) (.)\: (\w+)', text):
        total += p.count(c) in range(int(x), int(y)+1)
    return total


def test():
    aoc.test_subject(solve)
    aoc.test("""
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
""") == 2


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
