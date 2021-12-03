#!/usr/bin/env python
from collections import defaultdict


def part1(data):
    grid = {(x+1j*y):0 for y,s in enumerate(data.splitlines()) for x,c in enumerate(s) if c == 'L'}
    offs = (-1-1j, -1j, 1-1j, -1, 1, -1+1j, 1j, 1+1j)
    while True:
        new = dict()
        updated = False
        for k, v in grid.items():
            neib = sum(grid.get(k + i, 0) for i in offs)
            if v and (neib >= 4):
                v = 0
                updated = True
            elif (not v) and (not neib):
                v = 1
                updated = True
            new[k] = v
        if not updated: break
        grid = new
    return sum(grid.values())


def part1(data):
    lines = data.splitlines()
    grid = {(x,y):0 for y,s in enumerate(lines) for x,c in enumerate(s) if c == 'L'}
    w,h = len(lines[0]), len(lines)
    adj = defaultdict(set)
    for k in grid.keys():
        x,y = k
        for dx, dy in [(1,0), (0,1), (1,1), (-1,1)]:
            q = x+dx, y+dy
            if q in grid:
                adj[k].add(q)
                adj[q].add(k)
    
    while True:
        new = dict()
        updated = False
        for k, v in grid.items():
            neib = sum(grid[q] for q in adj[k])
            if v and (neib >= 4):
                v = 0
                updated = True
            elif (not v) and (not neib):
                v = 1
                updated = True
            new[k] = v
        if not updated: break
        grid = new
    return sum(grid.values())


def part2(data):
    lines = data.splitlines()
    grid = {(x,y):0 for y,s in enumerate(lines) for x,c in enumerate(s) if c == 'L'}
    w,h = len(lines[0]), len(lines)
    adj = defaultdict(set)
    for k in grid.keys():
        x,y = k
        for dx, dy in [(1,0), (0,1), (1,1), (-1,1)]:
            qx, qy = x+dx, y+dy
            while (0 <= qx < w) and (0 <= qy < h):
                q = (qx, qy)
                if q in grid:
                    adj[k].add(q)
                    adj[q].add(k)
                    break
                qx += dx
                qy += dy
    
    while True:
        new = dict()
        updated = False
        for k, v in grid.items():
            neib = sum(grid[q] for q in adj[k])
            if v and (neib >= 5):
                v = 0
                updated = True
            elif (not v) and (not neib):
                v = 1
                updated = True
            new[k] = v
        if not updated: break
        grid = new
    return sum(grid.values())


data = '''
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
'''.strip()
assert part1(data) == 37
assert part2(data) == 26


data = open('day11.in').read()
print(part1(data))
print(part2(data))
