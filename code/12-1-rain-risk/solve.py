#!/usr/bin/env python
import aocpaiv as aoc


def solve(text):
    pos = 0
    direction = 1
    rotate_right = {90: 1j, 180: -1, 270: -1j}
    rotate_left = {90: -1j, 180: -1, 270: 1j}
    for op in text.split():
        s, n = op[0], int(op[1:])
        if s == 'F':
            pos += direction * n
        elif s == 'N':
            pos += n * -1j
        elif s == 'S':
            pos += n * 1j
        elif s == 'E':
            pos += n
        elif s == 'W':
            pos += -n
        elif s == 'R':
            direction *= rotate_right[n]
        elif s == 'L':
            direction *= rotate_left[n]

    return int(abs(pos.real) + abs(pos.imag))


def test():
    aoc.test_subject(solve)

    aoc.test("""
F10
N3
F7
R90
F11
""") == 25


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
