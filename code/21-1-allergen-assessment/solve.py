#!/usr/bin/env python
import aocpaiv as aoc
import re
from collections import Counter
from functools import reduce


def solve(text):
    allergens = dict()
    ingredients = Counter()

    for m in re.finditer(r'^(.*?) \(contains (.*?)\)', text, re.M):
        ing = set(m[1].split())
        alg = [s.strip() for s in m[2].split(',')]

        ingredients.update(ing)

        for k in alg:
            x = allergens.get(k, set())
            allergens[k] = (x & ing) if x else ing

    bad = reduce(set.__or__, allergens.values())
    fine = set(ingredients.keys()) - bad
    return sum(ingredients[x] for x in fine)


def test():
    aoc.test_subject(solve)
    aoc.test("""
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
""") == 5


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
