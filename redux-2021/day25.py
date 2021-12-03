#!/usr/bin/env python
import itertools


def part1(data, P=20201227):
    pub1, pub2 = map(int, data.split())
    # card pub = 7^E mod P
    # door pub = 7^D mod P
    # priv = (card pub)^D mod P = (door pub)^E mod P
    for x in itertools.count(1):
        y = pow(7, x, P)
        if y == pub1:
            return pow(pub2, x, P)
        elif y == pub2:
            return pow(pub1, x, P)


def part2(data):
    return 50


data = '''
5764801
17807724
'''.strip()
assert part1(data) == 14897079
assert part2(data) == 50


data = open('day25.in').read()
print(part1(data))
print(part2(data))