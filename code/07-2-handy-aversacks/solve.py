#!/usr/bin/env python
import aocpaiv as aoc
import re


def solve(text):
    def parse_line(s):
        bag, rule = s.split('bags contain')
        return bag.strip(), re.findall(r'(\d+) (.*?) bag', rule)

    rules = dict(map(parse_line, text.strip().splitlines()))

    def sizeit(bag):
        fringe = [(bag, 1)]
        total = 0
        while fringe:
            bag, n = fringe.pop()
            for x, bag in rules[bag]:
                total += n * int(x)
                fringe.append((bag, n * int(x)))
        return total

    return sizeit('shiny gold')


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
""") == 32

    aoc.test("""
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
""") == 126


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
