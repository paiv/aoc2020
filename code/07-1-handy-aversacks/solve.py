#!/usr/bin/env python
import aocpaiv as aoc
import re


def solve(text):
    def parse_line(s):
        bag, rule = s.split('bags contain')
        return bag.strip(), re.findall(r'\d+ (.*?) bag', rule)

    rules = dict(map(parse_line, text.strip().splitlines()))

    def hasit(bag, goal='shiny gold'):
        if bag == goal: return False
        seen = set()
        fringe = [bag]
        while fringe:
            bag = fringe.pop()
            if bag == goal: return True
            seen.add(bag)
            for bag in rules[bag]:
                if bag not in seen:
                    fringe.append(bag)
        return False

    return sum(map(hasit, rules))


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
