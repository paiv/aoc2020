#!/usr/bin/env python
import aocpaiv as aoc
import re


def solve(text):
    rules, my_ticket, tickets = text.strip().split('\n\n')

    rule_names = re.findall(r'^([^:]+):', rules, re.M)
    rules = [[range(int(x), int(y)+1) for x, y in re.findall(r'(\d+)\-(\d+)', s)] for s in rules.splitlines()]
    my_ticket = [int(x) for x in re.findall(r'\d+', my_ticket)]
    tickets = [[int(x) for x in re.findall(r'\d+', s)] for s in tickets.splitlines()[1:]]

    def is_valid_value(x):
        for rx in rules:
            for r in rx:
                if x in r: return True
        return False

    def is_valid_ticket(ticket):
        return all(map(is_valid_value, ticket))

    valid_tickets = list(filter(is_valid_ticket, tickets))

    def all_passing(rule, xs):
        for x in xs:
            for r in rule:
                if x in r: break
            else:
                return False
        return True

    def matching_rules(xs):
        res = set()
        for i, rule in enumerate(rules):
            if all_passing(rule, xs):
                res.add(i)
        return res

    possible = dict()
    for i in range(len(rules)):
        col = [row[i] for row in valid_tickets]
        matching = matching_rules(col)
        possible[i] = matching

    coding = dict()
    for _, i, matching in sorted((len(v), k, v) for k,v in possible.items()):
        xs = matching - set(coding.values())
        coding[i] = xs.pop()

    res = 1
    for i, x in enumerate(my_ticket):
        s = rule_names[coding[i]]
        if s.startswith('departure'):
            res *= x

    return res


if __name__ == '__main__':
    print(solve(aoc.read_files()))
