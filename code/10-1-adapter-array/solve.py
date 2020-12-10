#!/usr/bin/env python
import aocpaiv as aoc
from collections import Counter


def solve(text):
    xs = sorted(map(int, text.split()))
    xs = [0] + xs + [xs[-1] + 3]

    cs = Counter((y-x) for x, y in zip(xs, xs[1:]))
    a, b = cs[1], cs[3]
    return a * b


def test():
    aoc.test_subject(solve)
    aoc.test("""
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
""") == 35

    aoc.test("""
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
""") == 220


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
