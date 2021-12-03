#!/usr/bin/env python
import re
from collections import defaultdict


def part1(data):
    rules = [range(int(x), int(y)+1) for x,y in re.findall(r'(\d+)-(\d+)', data)]
    tickets = data.split('nearby tickets')[1]
    ans = sum(x for x in (int(m[0]) for m in re.finditer(r'\d+', tickets))
        if all(x not in r for r in rules))
    return ans


def part2(data):
    rules, my_ticket, nearby = data.split('\n\n')
    my_ticket = [int(x) for x in re.findall(r'\d+', my_ticket)]
    ranges = [range(int(x), int(y)+1) for x,y in re.findall(r'(\d+)-(\d+)', rules)]
    tickets = [[int(x) for x in re.findall(r'\d+', s)] for s in nearby.splitlines()[1:]]
    tickets = [t for t in tickets if all(any(x in r for r in ranges) for x in t)]

    rules = {n:{range(int(x), int(y)+1) for x,y in re.findall(r'(\d+)-(\d+)', t)}
        for s in rules.splitlines()
        for n,t in [s.split(':')]}
    names = list(rules.keys())

    stats = defaultdict(set)
    for i in range(len(names)):
        col = [t[i] for t in tickets]
        for k, rs in rules.items():
            if all(any(x in r for r in rs) for x in col):
                stats[i].add(k)
    
    mapping = dict()
    for k, ns in sorted(stats.items(), key=lambda p: len(p[1])):
        xs = ns - set(mapping.values())
        mapping[k] = xs.pop()

    ans = 1
    for i, k in mapping.items():
        if k.startswith('departure'):
            ans *= my_ticket[i]
        
    return ans


data = '''
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
'''.strip()
assert part1(data) == 71
assert part2(data) == 1


data = open('day16.in').read()
print(part1(data))
print(part2(data))
