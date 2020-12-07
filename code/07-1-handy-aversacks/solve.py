#!/usr/bin/env python
import aocpaiv as aoc
import re
from collections import defaultdict


def solve(text):
    def parse_line(s):
        bag, rule = s.split('bags contain')
        return bag.strip(), re.findall(r'\d+ (.*?) bag', rule)

    parents = defaultdict(set)
    for bag, xs in map(parse_line, text.strip().splitlines()):
        for inner in xs:
            parents[inner].add(bag)

    total = 0
    fringe = ['shiny gold']
    nasty = set()
    while fringe:
        bag = fringe.pop()
        for p in parents[bag]:
            nasty.add(p)
            fringe.append(p)

    return len(nasty)


def test():
    aoc.test_subject(solve)
    aoc.test("""
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
""") == 4


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
