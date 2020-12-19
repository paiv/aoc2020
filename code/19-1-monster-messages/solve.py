#!/usr/bin/env python -OO
import aocpaiv as aoc
import functools
import re


def solve(text):
    rules, messages = text.strip().split('\n\n')
    rules = {int(i):s for i, s in re.findall(r'^(\d+):\s+(.*?)$', rules, re.M)}

    @functools.cache
    def emit(rule):
        text = rules[int(rule)]
        if (m := re.fullmatch(r'"(a|b)"', text)):
            return m[1]

        def seq(text):
            return ''.join(map(emit, text.split()))

        parts = [seq(p) for p in text.split('|')]
        if len(parts) > 1:
            s = '|'.join(parts)
            return f'(?:{s})'
        return ''.join(parts)


    rx0 = f'^{emit(0)}$'
    aoc.trace(rx0)
    rx0 = re.compile(rx0)

    return sum(bool(rx0.search(s)) for s in messages.splitlines())


def test():
    aoc.test_subject(solve)
    aoc.test("""
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
""") == 2


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
