#!/usr/bin/env python


def part1(data):
    data = sorted(map(int, data.split()))
    y = d1 = d3 = 0
    for x in data:
        d1 += (x - y == 1)
        d3 += (x - y == 3)
        y = x
    return d1 * (d3 + 1)


def part2(data):
    data = [0] + sorted(map(int, data.split()))
    m = [0] * len(data)
    m[0] = 1
    for i,x in enumerate(data):
        for j,y in enumerate(data[i+1:i+4], i+1):
            if y - x > 3: break
            m[j] += m[i]
    return m[-1]


data = '''
16
10
15
5
1
11
7
19
6
12
4
'''.strip()
assert part1(data) == 35
assert part2(data) == 8

data = '''
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
'''.strip()
assert part1(data) == 220
assert part2(data) == 19208

data = open('day10.in').read()
print(part1(data))
print(part2(data))
