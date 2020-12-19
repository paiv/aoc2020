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
    rules[8] = '42 | 42 8'
    rules[11] = '42 31 | 42 11 31'

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

    def repeated_match(rx, text, off):
        n = 0
        while (res := rx.match(text, off)):
            n += 1
            off = res
        return n, off

    rx42 = emit(42)
    rx31 = emit(31)

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


if __name__ == '__main__':
    with open(sys.argv[1]) as fp:
        text = fp.read()
    print(solve(text))
