#!/usr/bin/env python
import aocpaiv as aoc
import array


def solve(text, N=30000000):
    xs = list(map(int, text.split(',')))

    seen = array.array('I', [0]) * N

    for i, x in enumerate(xs, 1):
        seen[x] = i
    x = 0
    for i in range(len(xs)+1, N+1):
        res = x
        p = seen[x] or i
        seen[x] = i
        x = i - p

    return res


def test():
    aoc.test_subject(solve)
    aoc.test('0,3,6') == 175594
    aoc.test('1,3,2') == 2578
    aoc.test('2,1,3') == 3544142
    aoc.test('1,2,3') == 261214
    aoc.test('2,3,1') == 6895259
    aoc.test('3,2,1') == 18
    aoc.test('3,1,2') == 362


if __name__ == '__main__':
    # test()
    print(solve(aoc.read_files()))
