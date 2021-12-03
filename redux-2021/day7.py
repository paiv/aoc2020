#!/usr/bin/env python
import re


def part1(data):
    rules = dict()
    for bag, s in re.findall(r'^(.*?) bags contain (.*)$', data, re.M):
        for inner in re.findall(r'\d+ (.*?) bags?', s):
            xs = rules.get(inner, set())
            xs.add(bag)
            rules[inner] = xs

    fringe = ['shiny gold']
    seen = set()
    while fringe:
        p = fringe.pop()
        if p in seen: continue
        seen.add(p)
        for k in rules.get(p, set()):
            fringe.append(k)
    return len(seen)-1


def part2(data):
    rules = dict()
    for bag, s in re.findall(r'^(.*?) bags contain (.*)$', data, re.M):
        rules[bag] = re.findall(r'(\d+) (.*?) bags?', s)
                
    fringe = [(1, 'shiny gold')]
    total = 0
    while fringe:
        n, k = fringe.pop()
        total += n
        for i, p in rules.get(k, set()):
            fringe.append((int(i) * n, p))
    return total-1


data = '''
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
'''.strip()
assert part1(data) == 4
assert part2(data) == 32

data = '''
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
'''.strip()
assert part2(data) == 126


data = open('day7.in').read()
print(part1(data))
print(part2(data))
