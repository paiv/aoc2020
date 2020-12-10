#!/usr/bin/env python
import aocpaiv as aoc


def solve(text):
    xs = sorted(map(int, text.split()))
    xs = [0] + xs + [xs[-1] + 3]
    m = [0] * len(xs)
    m[0] = 1

    for i, x in enumerate(xs):
        for j in range(i+1, len(xs)):
            if (xs[j] - x) in range(1, 4):
                m[j] += m[i]
            else:
                break

    return m[-1]


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
""") == 8

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
""") == 19208


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
