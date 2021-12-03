#!/usr/bin/env python
import array


class Node:
    def __init__(self, x):
        self.x = x
        self.next = None

    def __repr__(self):
        n = self.next.x if self.next else '?'
        return f'{self.x}->{n}'


def part1(data, N=100):
    xs = [Node(int(x)) for x in data]
    p = xs[-1]
    p.next = xs[0]
    for n in xs[:-1][::-1]:
        n.next = p
        p = n

    def walk(p, n=9):
        while n:
            yield p
            p = p.next
            n -= 1
    # print(list(walk(xs[0])))

    p = xs[0]
    for _ in range(N):
        u,v = p.next, p.next.next.next
        p.next = v.next
        q = p.next
        a = z = Node(-1)
        while q != p:
            if z.x < q.x < p.x:
                z = q
            if a.x < q.x > p.x:
                a = q
            q = q.next
        if z.x == -1:
            z = a
        v.next = z.next
        z.next = u
        p = p.next
        # print(list(walk(p)))

    p = next(n for n in xs if n.x == 1)
    ans = sum((10**(7-i) * n.x) for i,n in enumerate(walk(p.next, 8)))
    return ans


def part1(data, N=100):
    cups = list(map(int, data))
    edge = array.array('I', [0]) * 10
    for i, x in enumerate(cups, 1):
        edge[x] = cups[i % len(cups)]

    p = cups[0]
    for _ in range(N):
        x = edge[p]
        y = edge[x]
        z = edge[y]

        q = (p - 2) % 9 + 1
        while q == x or q == y or q == z:
            q = (q - 2) % 9 + 1

        edge[p] = edge[z]
        p = edge[p]
        edge[z] = edge[q]
        edge[q] = x

    ans = 0
    p = edge[1]
    while p != 1:
        ans = ans * 10 + p
        p = edge[p]

    return ans


def part2(data, N=10_000_000, M=1_000_000):
    cups = list(map(int, data))
    edge = array.array('I', [0]) * (M + 1)
    for i, x in enumerate(cups, 1):
        edge[x] = cups[i % len(cups)]
    edge[cups[-1]] = t = max(cups) + 1
    for x in range(t, M):
        edge[x] = x + 1
    edge[M] = cups[0]

    p = cups[0]
    for _ in range(N):
        x = edge[p]
        y = edge[x]
        z = edge[y]

        q = (p - 2) % M + 1
        while q == x or q == y or q == z:
            q = (q - 2) % M + 1

        edge[p] = edge[z]
        p = edge[p]
        edge[z] = edge[q]
        edge[q] = x

    x = edge[1]
    y = edge[x]
    return x * y


data = '389125467'
assert part1(data) == 67384529
assert part2(data) == 149245887792


data = open('day23.in').read()
print(part1(data))
print(part2(data))