#!/usr/bin/env python
import itertools
import re
from functools import reduce


def part1(data):
    foods = [(set(i.split()), set(x.strip() for x in a.split(',')))
        for i,a in re.findall(r'^(.*?)\s*\(contains\s+(.*?)\)$', data, re.M)]

    alg_ing = dict()
    for ings, algs in foods:
        for a in algs:
            xs = alg_ing.get(a, set())
            xs = (xs & ings) if xs else ings
            alg_ing[a] = xs

    bad = reduce(set.union, alg_ing.values())
    ans = sum(len(ings - bad) for ings, _ in foods)
    return ans


def part2(data):
    foods = [(set(i.split()), set(x.strip() for x in a.split(',')))
        for i,a in re.findall(r'^(.*?)\s*\(contains\s+(.*?)\)$', data, re.M)]

    alg_ing = dict()
    for ings, algs in foods:
        for a in algs:
            xs = alg_ing.get(a, set())
            xs = (xs & ings) if xs else ings
            alg_ing[a] = xs

    bad = reduce(set.union, alg_ing.values())
    seen = set()
    while seen != bad:
        for ings in alg_ing.values():
            if len(ings) > 1:
                ings -= seen
            if len(ings) == 1:
                seen |= ings

    ans = ','.join(v.pop() for _, v in sorted(alg_ing.items()))
    return ans


data = '''
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
'''.strip()
assert part1(data) == 5
assert part2(data) == 'mxmxvkd,sqjhc,fvjkl'


data = open('day21.in').read()
print(part1(data))
print(part2(data))