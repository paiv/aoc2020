#!/usr/bin/env python
import itertools


def part1(data):
    data = [int(x) for x in data.split()]
    for i,x in enumerate(data):
        for y in data[i+1:]:
            if x + y == 2020:
                return x * y


def part2(data):
    data = [int(x) for x in data.split()]
    for i,x in enumerate(data):
        for j,y in enumerate(data[i+1:], i+1):
            for z in data[j+1:]:
                if x + y + z == 2020:
                    return x * y * z

def part2(data):
    data = [int(x) for x in data.split()]
    for x, y, z in itertools.combinations(data, 3):
        if x + y + z == 2020:
            return x * y * z


data = '''
1721
979
366
299
675
1456
'''.strip()
assert part1(data) == 514579
assert part2(data) == 241861950


data = open('day1.in').read()
print(part1(data))
print(part2(data))