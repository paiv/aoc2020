#!/usr/bin/env python
import aocpaiv as aoc
import re


def solve(text):
    color_rx = re.compile(r'^#[0-9a-f]{6}$')
    eye_colors = set('amb blu brn gry grn hzl oth'.split())
    validators = {
        'byr': lambda v: 1920 <= int(v) <= 2002,
        'iyr': lambda v: 2010 <= int(v) <= 2020,
        'eyr': lambda v: 2020 <= int(v) <= 2030,
        'hgt': lambda v: (v.endswith('cm') and (150 <= int(v[:-2]) <= 193)) or
                         (v.endswith('in') and (59 <= int(v[:-2]) <= 76)),
        'hcl': lambda v: color_rx.match(v) != None,
        'ecl': lambda v: v in eye_colors,
        'pid': lambda v: len(v) == 9 and v.isdigit(),
        'cid': lambda v: True,
    }
    def valid(batch):
        batch = dict(p.split(':') for p in batch.split())
        expect = set(validators)
        if (set(batch) | {'cid'}) & expect != expect:
            return False
        for k,v in batch.items():
            if not validators[k](v):
                return False
        return True

    return sum(map(valid, text.split('\n\n')))


def test():
    aoc.test_subject(solve)
    aoc.test("""
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
""") == 2


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
