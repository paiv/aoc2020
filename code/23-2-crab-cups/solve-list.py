#!/usr/bin/env python
import aocpaiv as aoc


def solve(text, N=10000000, M=1000000):
    cups = Node(0)
    p = cups.extend(map(int, text.strip()))
    last = p.extend(range(len(text.strip())+1, M+1))
    cups = cups.next
    last.next = cups

    nodes = {cups.value:cups}
    it = cups.next
    while it != cups:
        nodes[it.value] = it
        it = it.next

    for round in range(N):
        if round % 100000 == 0:
            aoc.trace(round)
        x = cups.value
        while True:
            it = cups
            for _ in range(4):
                if x == it.value:
                    x = (x - 2) % M + 1
                    break
                it = it.next
            else: break
        it = nodes[x]
        it.xpaste(cups, 3)
        cups = cups.next

    it = nodes[1].next
    x, it = it.value, it.next
    y = it.value
    return x * y


class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.next = None
        if parent:
            parent.next = self

    class Iterator:
        def __init__(self, node):
            self.start = node
            self.next = node

        def __next__(self):
            if self.next is None: raise StopIteration()
            v = self.next.value
            self.next = self.next.next if (self.next.next != self.start) else None
            return v

    def __iter__(self):
        return Node.Iterator(self)

    def append(self, v):
        t = self.next
        n = Node(v, self)
        n.next = t
        return n

    def extend(self, iterable):
        for x in iterable:
            self = Node(x, self)
        return self

    def pop(self):
        v = self.value
        self.value = self.next.value
        self.next = self.next.next
        return v

    def xpaste(self, prev, n):
        start = prev.next
        end = prev
        for _ in range(n):
            end = end.next
        prev.next = end.next
        end.next, self.next = self.next, start


def test():
    aoc.test_subject(solve)
    aoc.test('389125467') == 149245887792


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
