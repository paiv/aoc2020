#!/usr/bin/env python
import re
import sys


class Node:
    def __init__(self):
        pass


class Term (Node):
    def __init__(self, t):
        super().__init__()
        self.t = t

    def match(self, text, off=0):
        if off < len(text) and text[off] == self.t:
            return off + 1


class Seq (Node):
    def __init__(self, seq):
        super().__init__()
        self.seq = seq

    def match(self, text, off=0):
        for t in self.seq:
            off = t.match(text, off)
            if off is None: break
        return off


class Alt (Node):
    def __init__(self, seq):
        super().__init__()
        self.seq = seq

    def match(self, text, off=0):
        for t in self.seq:
            res = t.match(text, off)
            if res is not None:
                return res


def solve(text):
    rules, messages = text.strip().split('\n\n')
    rules = {int(i):s for i, s in re.findall(r'^(\d+):\s+(.*?)$', rules, re.M)}

    def emit(rule):
        text = rules[int(rule)]
        if (m := re.fullmatch(r'"(a|b)"', text)):
            return Term(m[1])

        def seq(text):
            return Seq([emit(s) for s in text.split()])

        parts = [seq(p) for p in text.split('|')]
        if len(parts) > 1:
            return Alt(parts)
        return parts[0]

    rx0 = emit(0)

    def rx0_match(text):
        off = rx0.match(text)
        return off == len(text)

    return sum(rx0_match(s) for s in messages.splitlines())


if __name__ == '__main__':
    with open(sys.argv[1]) as fp:
        text = fp.read()
    print(solve(text))
