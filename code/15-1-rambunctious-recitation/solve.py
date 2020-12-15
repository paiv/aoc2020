#!/usr/bin/env python
import aocpaiv as aoc


def solve(text, N=2020):
    xs = list(map(int, text.split(',')))

    seen = {x:i for i, x in enumerate(xs)}
    x = 0

    for i in range(len(xs), N):
        res = x
        p = seen.get(x, i)
        seen[x] = i
        x = i - p

    return res


def test():
    aoc.test_subject(solve)
    aoc.test('0,3,6') == 436
    aoc.test('1,3,2') == 1
    aoc.test('2,1,3') == 10
    aoc.test('1,2,3') == 27
    aoc.test('2,3,1') == 78
    aoc.test('3,2,1') == 438
    aoc.test('3,1,2') == 1836


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
