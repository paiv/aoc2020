#!/usr/bin/env python
import aocpaiv as aoc
import re


def solve(text):
    mem = dict()

    def masked(x, mask):
        for i, b in mask:
            x &= ~(1 << i)
            x |= (b << i)
        return x

    for m in re.finditer(r'(?:mask|mem\[(\d+)\]) = ([X\d]+)', text):
        addr, value = m[1], m[2]
        if addr is None:
            mask = [(35-i, int(x)) for i,x in enumerate(value) if x in '01']
        else:
            mem[int(addr)] = masked(int(value), mask)

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
