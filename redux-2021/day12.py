#!/usr/bin/env python

def part1(data):
    pos = 0j
    direction = 1+0j
    angles = {'R90': 1j, 'R180': -1, 'R270': -1j,
        'L90': -1j, 'L180': -1, 'L270': 1j}
    for sop in data.splitlines():
        op, n = sop[0], int(sop[1:])
        if op == 'F':
            pos += direction * n
        elif op == 'N':
            pos += -1j * n
        elif op == 'S':
            pos += 1j * n
        elif op == 'E':
            pos += n
        elif op == 'W':
            pos += -n
        elif op == 'L':
            direction *= angles[sop]
        elif op == 'R':
            direction *= angles[sop]
    return int(abs(pos.real) + abs(pos.imag))


def part2(data):
    pos = 0j
    waypoint = 10-1j
    right = {90: 1j, 180: -1, 270: -1j}
    left = {90: -1j, 180: -1, 270: 1j}
    ops = {
        'F': lambda x: (pos + waypoint * x, waypoint),
        'N': lambda x: (pos, waypoint - 1j * x),
        'S': lambda x: (pos, waypoint + 1j * x),
        'E': lambda x: (pos, waypoint + x),
        'W': lambda x: (pos, waypoint - x),
        'L': lambda x: (pos, waypoint * left[x]),
        'R': lambda x: (pos, waypoint * right[x]),
    }
    for sop in data.splitlines():
        op, n = sop[0], int(sop[1:])
        pos, waypoint = ops[op](n)

    return int(abs(pos.real) + abs(pos.imag))


data = '''
F10
N3
F7
R90
F11
'''.strip()
assert part1(data) == 25
assert part2(data) == 286


data = open('day12.in').read()
print(part1(data))
print(part2(data))
