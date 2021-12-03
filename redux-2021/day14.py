#!/usr/bin/env python
import itertools
import re


def part1(data):
    def pmask(s):
        return (sum((2**i) for i,x in enumerate(s[::-1]) if x != '0'),
            sum((2**i) for i,x in enumerate(s[::-1]) if x == '1'))
    def masked(x, m):
        return x & m[0] | m[1]
        
    mem = dict()
    mask = None
    for m,a,x in re.findall(r'mask\s*=\s*(\S+)|mem\[(\d+)\]\s*=\s*(\d+)', data):
        if m:
            mask = pmask(m)
        else:
            mem[int(a)] = masked(int(x), mask)
    return sum(mem.values())


def part2(data):
    def pmask(s):
        return (sum((1 << i) for i,x in enumerate(s[::-1]) if x == '1'),
            [i for i,x in enumerate(s[::-1]) if x == 'X'])
    def masked(x, m):
        ones, xi = m
        for p in itertools.product(*([(i,0), (i,1)] for i in xi)):
            y = x | ones
            for i, t in p:
                if t:
                    y |= (t << i)
                else:
                    y &= ~(1 << i)
            yield y

    mem = dict()
    mask = None
    for m,a,x in re.findall(r'mask\s*=\s*(\S+)|mem\[(\d+)\]\s*=\s*(\d+)', data):
        if m:
            mask = pmask(m)
        else:
            for p in masked(int(a), mask):
                mem[p] = int(x)
    return sum(mem.values())


data = '''
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
'''.strip()
assert part1(data) == 165

data = '''
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
'''.strip()
assert part2(data) == 208


data = open('day14.in').read()
print(part1(data))
print(part2(data))
