#!/usr/bin/env python
import re

def part1(data):
    def valid(s):
        r, p = s.split(':')
        x,c = r.split()
        x,y = map(int, x.split('-'))
        return p.count(c) in range(x, y+1)
    return sum(map(valid, data.splitlines()))
    

def part1(data):
    rx = re.compile(r'(\d+)-(\d+)\s+(\w):\s+(\S+)')
    def valid(s):
        (x,y,c,p), = rx.findall(s)
        x,y = int(x), int(y)
        return p.count(c) in range(x, y+1)
    return sum(map(valid, data.splitlines()))


def part2(data):
    def valid(s):
        r, p = s.split(':')
        x,c = r.split()
        x,y = map(int, x.split('-'))
        return (p[x] == c) ^ (p[y] == c)
    return sum(map(valid, data.splitlines()))

    
data = '''
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
'''.strip()
assert part1(data) == 2
assert part2(data) == 1

data = open('day2.in').read()
print(part1(data))
print(part2(data))
