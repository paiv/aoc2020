#!/usr/bin/env python
import aocpaiv as aoc


def solve(text):
    pos = 0
    waypoint = 10-1j
    rotate_right = {90: 1j, 180: -1, 270: -1j}
    rotate_left = {90: -1j, 180: -1, 270: 1j}
    for op in text.split():
        s, n = op[0], int(op[1:])
        if s == 'F':
            pos += waypoint * n
        elif s == 'N':
            waypoint += n * -1j
        elif s == 'S':
            waypoint += n * 1j
        elif s == 'E':
            waypoint += n
        elif s == 'W':
            waypoint += -n
        elif s == 'R':
            waypoint *= rotate_right[n]
        elif s == 'L':
            waypoint *= rotate_left[n]

    return int(abs(pos.real) + abs(pos.imag))


def test():
    aoc.test_subject(solve)

    aoc.test("""
F10
N3
F7
R90
F11
""") == 286


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
