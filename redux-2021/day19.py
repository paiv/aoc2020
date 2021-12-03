#!/usr/bin/env python
import re


def part1(data):
    rules, messages = data.split('\n\n')
    rules = {k:s for k,s in re.findall(r'^(\d+):\s*(.*?)$', rules, re.M)}
    def makerx(sid):
        def ml(s):
            if s.startswith('"'): return s[1:-1]
            return ''.join(makerx(x) for x in s.split())
        t = rules[sid]
        if '|' in t:
            s = '|'.join(f'{ml(p.strip())}' for p in t.split('|'))
            return f'(?:{s})'
        return ml(t)
    rx = makerx('0')
    rx = re.compile(f'^(?:{rx})$', re.M)
    ans = sum(1 for m in rx.finditer(messages))
    return ans


def part2(data):
    rules, messages = data.split('\n\n')
    rules = {k:s for k,s in re.findall(r'^(\d+):\s*(.*?)$', rules, re.M)}
    del rules['8']
    del rules['11']

    def makerx(sid):
        def ml(s):
            if s.startswith('"'): return s[1:-1]
            return ''.join(makerx(x) for x in s.split())
        t = rules[sid]
        if '|' in t:
            s = '|'.join(f'{ml(p.strip())}' for p in t.split('|'))
            return f'(?:{s})'
        return ml(t)

    # 8: 42 | 42 8
    rx42 = re.compile(makerx('42'))
    # 11: 42 31 | 42 11 31
    rx31 = re.compile(makerx('31'))
    # 0: 8 11
    # rx = f'^{r42}+?({r42}\\1*{r31})$' # re.error: cannot refer to an open group

    def match0(text):
        pos = 0
        n = p = 0
        while (m := rx42.match(text, pos)):
            pos = m.end()
            n += 1
        while (m := rx31.match(text, pos)):
            pos = m.end()
            p += 1
        return (pos == len(text)) and (0 < p < n)

    ans = sum(match0(s) for s in messages.splitlines())
    return ans


data = '''
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
'''.strip()
assert part1(data) == 2


data = '''
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
'''
assert part2(data) == 12


data = open('day19.in').read()
print(part1(data))
print(part2(data))