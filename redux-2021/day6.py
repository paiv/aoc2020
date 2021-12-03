#!/usr/bin/env python
from functools import reduce

def part1(data):
    return sum(len(set(x for q in s.split() for x in q)) for s in data.split('\n\n'))
    
def part2(data):
    return sum(len(reduce(set.intersection, map(set, s.split()))) for s in data.split('\n\n'))
    
data = '''
abc

a
b
c

ab
ac

a
a
a
a

b
'''.strip()
assert part1(data) == 11
assert part2(data) == 6

data = open('day6.in').read()
print(part1(data))
print(part2(data))
