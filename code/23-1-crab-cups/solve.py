#!/usr/bin/env python
import aocpaiv as aoc


def solve(text, N=100):
    cups = list(map(int, text.strip()))
    p = 0
    for round in range(N):
        cur = cups[p]
        removed = list()
        for _ in range(3):
            if p+1 < len(cups):
                removed.append(cups.pop(p+1))
            else:
                removed.append(cups.pop(0))
                p -= 1
        t = cur - 1
        while t in removed:
            t -= 1
        if not t:
            t = max(cups)
            while t in removed:
                t -= 1
        i = cups.index(t)
        cups[i+1:i+1] = removed
        p = (p + 1 + (3 if i <= p else 0)) % len(cups)

    i = cups.index(1)
    res = cups[i+1:] + cups[:i]
    return int(''.join(map(str, res)))


def test():
    aoc.test_subject(solve)
    aoc.test('389125467') == 67384529


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
