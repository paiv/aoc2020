#!/usr/bin/env python
import aocpaiv as aoc


def solve(text):
    ws = set(' \n')
    return sum(len(set(s) - ws) for s in text.split('\n\n'))


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
""") == 11


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
