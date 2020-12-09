#!/usr/bin/env python
import aocpaiv as aoc


def solve(text, n=25):
    def valid(xs, x):
        for i,a in enumerate(xs):
            for b in xs[i:]:
                if a + b == x: return True
        return False

    xs = aoc.parse_ints_flatten(text)

    for i, t in enumerate(xs[n:], n):
        if not valid(xs[i-n:i], t):
            break

    for i in range(len(xs)):
        for j in range(i+1, len(xs)+1):
            x = sum(xs[i:j])
            if x == t:
                return min(xs[i:j]) + max(xs[i:j])
            if x > t: break


def test():
    aoc.test_subject(solve)
    aoc.test("""
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
""", n=5) == 62


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
