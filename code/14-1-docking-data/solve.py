#!/usr/bin/env python
import aocpaiv as aoc
import re


def solve(text):
    mem = dict()

    def make_masks(value):
        ma = mb = 0
        for i,x in enumerate(reversed(value)):
            if x == '0':
                ma |= 1 << i
            elif x == '1':
                mb |= 1 << i
        return ~ma, mb

    for g in re.finditer(r'(?:mask|mem\[(\d+)\]) = ([X\d]+)', text):
        addr, value = g[1], g[2]
        if addr is None:
            ma, mb = make_masks(value)
        else:
            mem[int(addr)] = int(value) & ma | mb

    return sum(mem.values())


def test():
    aoc.test_subject(solve)
    aoc.test("""
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
""") == 165


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
