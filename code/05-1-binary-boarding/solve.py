#!/usr/bin/env python
import aocpaiv as aoc


def seatid(s):
    row = sum((1 << i) for i,x in enumerate(reversed(s[:-3])) if x == 'B')
    col = sum((1 << i) for i,x in enumerate(reversed(s[-3:])) if x == 'R')
    return row * 8 + col


def solve(text):
    return max(map(seatid, text.splitlines()))


def test():
    aoc.test_subject(seatid)
    aoc.test('FBFBBFFRLR') == 357


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
