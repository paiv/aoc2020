#!/usr/bin/env python
import aocpaiv as aoc
import functools
import re


def solve(text):
    rules, messages = text.strip().split('\n\n')
    rules = {int(i):s for i, s in re.findall(r'^(\d+):\s+(.*?)$', rules, re.M)}
    rules[8] = '42 | 42 8'
    rules[11] = '42 31 | 42 11 31'

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

    def repeated_match(rx, text, off):
        n = 0
        while (m := rx.match(text[off:])):
            n += 1
            off += len(m[0])
        return n, off

    rx31 = re.compile(emit(31))
    rx42 = re.compile(emit(42))

    def match8(text, off):
        return repeated_match(rx42, text, off)

    def match11(text, off):
        return repeated_match(rx31, text, off)

    def match0(text):
        n, off = match8(text, 0)
        if n > 1:
            m, off = match11(text, off)
            return (off == len(text)) and (m > 0) and (m < n)
        return False

    return sum(match0(s) for s in messages.splitlines())


def test():
    aoc.test_subject(solve)
    aoc.test("""
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
""") == 12


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
