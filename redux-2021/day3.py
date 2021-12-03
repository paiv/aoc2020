#!/usr/bin/env python

def traverse(grid, dx=3, dy=1):
    w = max(x for x, y in grid) + 1
    bottom = max(y for x, y in grid) + 1
    x = y = ans = 0
    while y < bottom:
        ans += (x % w, y) in grid
        x += dx
        y += dy
    return ans
    
def part1(data):
    grid = {(x,y) for y,s in enumerate(data.splitlines())
        for x,c in enumerate(s) if c == '#'}
    return traverse(grid, 3, 1)
    
def part2(data):
    grid = {(x,y) for y,s in enumerate(data.splitlines())
        for x,c in enumerate(s) if c == '#'}
    return (
        traverse(grid, 1, 1) *
        traverse(grid, 3, 1) *
        traverse(grid, 5, 1) *
        traverse(grid, 7, 1) *
        traverse(grid, 1, 2)
        )


data = '''
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
'''.strip()
assert part1(data) == 7
assert part2(data) == 336

data = open('day3.in').read()
print(part1(data))
print(part2(data))
