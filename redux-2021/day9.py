#!/usr/bin/env python


def part1(data, n=25):
    def check(m, x):
        for i,a in enumerate(m):
            for b in m[i+1:]:
                if a + b == x:
                    return True
        return False

    data = list(map(int, data.split()))
    for i,x in enumerate(data[n:], n):
        if not check(data[i-n:i], x):
            return x


def part2(data, n=25):
    q = part1(data, n)
    data = list(map(int, reversed(data.split())))
    for i,a in enumerate(data):
        m = x = y = a
        for j,b in enumerate(data[i+1:], i+1):
            m += b
            x = min(x, b)
            y = max(y, b)
            if m == q:
                return x + y
            elif m > q:
                break


data = '''
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
'''.strip()
assert part1(data, 5) == 127
assert part2(data, 5) == 62


data = open('day9.in').read()
print(part1(data))
print(part2(data))
