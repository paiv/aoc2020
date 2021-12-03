#!/usr/bin/env python
import re


def part1(data):
    t, *ids = map(int, re.findall(r'\d+', data))
    for i in range(1000):
        for x in ids:
            if (t + i) % x == 0:
                return i * x


def part1(data):
    t, *ids = map(int, re.findall(r'\d+', data))
    xs = [((x - t % x) % x, x) for x in ids]
    t, x = min(xs)
    return t * x


def part2(data):
    buses = [(int(x), i) for i, x in enumerate(data.splitlines()[1].split(',')) if x.isdigit()]
    buses = [(x, (x - i) % x) for x, i in buses]
    # chinese rmainder, sieve
    buses = sorted(buses, reverse=True)
    m, t = buses[0]
    for x, xt in buses[1:]:
        while (t % x != xt):
            t += m
        m *= x
    return t


data = '''
939
7,13,x,x,59,x,31,19
'''.strip()
assert part1(data) == 295
assert part2(data) == 1068781

examples = [
    ('17,x,13,19', 3417),
    ('67,7,59,61', 754018),
    ('67,x,7,59,61', 779210),
    ('67,7,x,59,61', 1261476),
    ('1789,37,47,1889', 1202161486),
]
for s, r in examples:
    assert part2('0\n'+s) == r, s

data = open('day13.in').read()
print(part1(data))
print(part2(data))
