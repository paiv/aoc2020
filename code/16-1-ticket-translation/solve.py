#!/usr/bin/env python
import aocpaiv as aoc
import re


def solve(text):
    rules, _, tickets = text.split('\n\n')

    rules = [range(int(x), int(y)+1) for x, y in re.findall(r'(\d+)\-(\d+)', rules)]

    def invalid(x):
        for r in rules:
            if x in r: return False
        return True

    values = map(int, re.findall(r'\d+', tickets))
    return sum(filter(invalid, values))


def test():
    aoc.test_subject(solve)
    aoc.test("""
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
""") == 71


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
