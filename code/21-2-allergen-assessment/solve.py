#!/usr/bin/env python
import aocpaiv as aoc
import re
from functools import reduce


def solve(text):
    allergens = dict()

    for m in re.finditer(r'^(.*?) \(contains (.*?)\)', text, re.M):
        ing = set(m[1].split())
        alg = [s.strip() for s in m[2].split(',')]
        for k in alg:
            x = allergens.get(k, set())
            allergens[k] = (x & ing) if x else ing

    bad = reduce(set.__or__, allergens.values())

    resolved = set()
    while len(resolved) < len(allergens):
        for k, xs in allergens.items():
            if len(xs) > 1:
                xs = allergens[k] = xs - resolved
            if len(xs) == 1:
                resolved |= xs

    res = [(k, v.pop()) for k,v in allergens.items()]
    return ','.join(v for k,v in sorted(res))


def test():
    aoc.test_subject(solve)
    aoc.test("""
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
""") == 'mxmxvkd,sqjhc,fvjkl'


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
