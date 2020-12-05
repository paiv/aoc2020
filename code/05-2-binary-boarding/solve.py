#!/usr/bin/env python
import aocpaiv as aoc


def seatid(s):
    row = sum((1 << i) for i,x in enumerate(reversed(s[:-3])) if x == 'B')
    col = sum((1 << i) for i,x in enumerate(reversed(s[-3:])) if x == 'R')
    return row * 8 + col


def encode_seat(seat):
    row, col = divmod(seat, 8)
    a = f'{row:07b}'.translate(str.maketrans('01', 'FB'))
    b = f'{col:03b}'.translate(str.maketrans('01', 'LR'))
    return a + b


def solve(text):
    xs = sorted(map(seatid, text.splitlines()))
    for a, b in zip(xs, xs[1:]):
        if b - a == 2:
            return a + 1


def test():
    aoc.test_subject(seatid)
    aoc.test('FBFBBFFRLR') == 357

    aoc.test_subject(encode_seat)
    aoc.test(357) == 'FBFBBFFRLR'


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
