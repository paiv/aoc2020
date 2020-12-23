#!/usr/bin/env python
import aocpaiv as aoc
import array


def solve(text, N=10000000, M=1000000):
    m = array.array('I')
    m.extend(range(M+1))
    xs = list(map(int, text.strip()))
    for i,x in enumerate(xs):
        m[x] = xs[(i+1) % len(xs)]
    x = max(xs) + 1
    m[xs[-1]] = x
    for _ in range(len(xs), M):
        m[x] = x = x + 1

    if M == 9:
        m[xs[-1]] = xs[0]
    else:
        m[xs[-1]] = max(xs)+1
        m[-1] = xs[0]

    p = xs[0]
    for _ in range(N):
        x = m[p]
        y = m[x]
        z = m[y]
        q = (p - 2) % M + 1
        while (q == x) or (q == y) or (q == z):
            q = (q - 2) % M + 1

        s = m[p]
        e = m[m[s]]
        m[p] = p = m[e]
        m[e], m[q] = m[q], s

    if M == 9:
        res = 0
        p = m[1]
        for _ in range(M-1):
            res = res * 10 + p
            p = m[p]
        return res

    x = m[1]
    y = m[x]
    return x * y


def test():
    aoc.test_subject(solve)
    aoc.test('389125467', N=100, M=9) == 67384529
    aoc.test('389125467') == 149245887792


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
