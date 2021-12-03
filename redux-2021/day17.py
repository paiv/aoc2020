#!/usr/bin/env python


def part1(data):
    grid = {(x,y,0):(c == '#') for y,s in enumerate(data.splitlines()) for x,c in enumerate(s)}
    adj = [(x-1,y-1,z-1) for z in range(3) for y in range(3) for x in range(3)
        if not (1 == z == y == x)]
    for _ in range(6):
        pois = set(grid.keys()) | set((x+dx,y+dy,z+dz) for (x,y,z) in grid.keys() for dx,dy,dz in adj)
        state = dict()
        for k in pois:
            (x,y,z) = k
            neib = sum(grid.get((x+dx,y+dy,z+dz),0) for dx,dy,dz in adj)
            if grid.get(k):
                if neib in (2,3):
                    state[k] = 1
            else:
                if neib == 3:
                    state[k] = 1
        grid = state
    return sum(grid.values())


def part2(data):
    grid = {(x,y,0,0):(c == '#') for y,s in enumerate(data.splitlines()) for x,c in enumerate(s)}
    adj = [(x-1,y-1,z-1,w-1) for w in range(3) for z in range(3) for y in range(3) for x in range(3)
        if not (1 == w == z == y == x)]
    for _ in range(6):
        pois = set(grid.keys()) | set((x+dx,y+dy,z+dz,w+dw) for (x,y,z,w) in grid.keys() for dx,dy,dz,dw in adj)
        state = dict()
        for k in pois:
            (x,y,z,w) = k
            neib = sum(grid.get((x+dx,y+dy,z+dz,w+dw),0) for dx,dy,dz,dw in adj)
            if grid.get(k):
                if neib in (2,3):
                    state[k] = 1
            else:
                if neib == 3:
                    state[k] = 1
        grid = state
    return sum(grid.values())


data = '''
.#.
..#
###
'''.strip()
assert part1(data) == 112
assert part2(data) == 848


data = open('day17.in').read()
print(part1(data))
print(part2(data))
