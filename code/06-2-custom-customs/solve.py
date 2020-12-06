#!/usr/bin/env python
import aocpaiv as aoc
import operator
from functools import reduce


def solve(text):
    return sum(len(reduce(operator.and_, map(set, s.split())))
        for s in text.split('\n\n'))


def test():
    aoc.test_subject(solve)
    aoc.test("""
abc

a
b
c

ab
ac

a
a
a
a

b
""") == 6


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
