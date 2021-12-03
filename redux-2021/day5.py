#!/usr/bin/env python

def seatid(s):
    return sum((2**(9-i)) for i,x in enumerate(s) if x in 'BR')

assert seatid('FBFBBFFRLR') == 357
assert seatid('BFFFBBFRRR') == 567
assert seatid('FFFBBBFRRR') == 119
assert seatid('BBFFBBFRLL') == 820

def part1(data):
    return max(map(seatid, data))
    
def part2(data):
    xs = sorted(map(seatid, data))
    for a,b in zip(xs, xs[1:]):
        if b - a == 2:
            return a + 1

data = open('day5.in').readlines()
print(part1(data))
print(part2(data))
