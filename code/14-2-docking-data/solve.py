#!/usr/bin/env python
import aocpaiv as aoc
import itertools
import re


def solve(text):
    mem = dict()

    def masked(x, mask):
        xs = [((i, 0), (i, 1)) for i, b in mask if b == 'X']
        for i, b in mask:
            if b == '1':
                x |= (1 << i)
        for p in itertools.product(*xs):
            m = x
            for i, b in p:
                m &= ~(1 << i)
                m |= (b << i)
                yield m

    for m in re.finditer(r'(?:mask|mem\[(\d+)\]) = ([X\d]+)', text):
        addr, value = m[1], m[2]
        if addr is None:
            mask = [(35-i, x) for i,x in enumerate(value) if x in '1X']
        else:
            for addr in masked(int(addr), mask):
                mem[addr] = int(value)

    return sum(mem.values())


def test():
    aoc.test_subject(solve)
    aoc.test("""
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
""") == 208


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
