#!/usr/bin/env python
import array


def part1(data):
    xs = list(map(int, data.split(',')))
    seen = dict()
    for t, x in enumerate(xs):
        seen[x] = t
    q = 0
    for t in range(t+1, 2020):
        x = q if q else 0
        q = t - seen.get(x, t)
        seen[x] = t
    return x


def part2(data, N=30000000):
    xs = list(map(int, data.split(',')))
    seen = array.array('I', [0]) * N
    for t, x in enumerate(xs,1):
        seen[x] = t
    q = 0
    for t in range(t+1, N+1):
        x = q if q else 0
        q = t - (seen[x] or t)
        seen[x] = t
    print(x)
    return x


examples = [
    ('0,3,6', 436),
    ('1,3,2', 1),
    ('2,1,3', 10),
    ('1,2,3', 27),
    ('2,3,1', 78),
    ('3,2,1', 438),
    ('3,1,2', 1836),
]
for s,r in examples:
    assert part1(s) == r, (s, r, part1(s))

examples = [
    ('0,3,6', 175594),
    ('1,3,2', 2578),
    ('2,1,3', 3544142),
    ('1,2,3', 261214),
    ('2,3,1', 6895259),
    ('3,2,1', 18),
    ('3,1,2', 362),
]
# for s,r in examples:
#     assert part2(s) == r, (s, r, part2(s))

data = open('day15.in').read()
print(part1(data))
print(part2(data))