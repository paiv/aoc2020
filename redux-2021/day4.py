#!/usr/bin/env python
import re

def part1(data):
    expected = set('byr iyr eyr hgt hcl ecl pid'.split())
    def valid(s):
        keys = {x.split(':')[0] for x in s.split()}
        return not (expected - keys)
    return sum(map(valid, data.split('\n\n')))

def part2(data):
    rx_color = re.compile(r'^#[0-9a-f]{6}$')
    colors = set('amb blu brn gry grn hzl oth'.split())
    height = lambda s, a, b, fx: s.endswith(fx) and s[:-len(fx)].isdigit() and a <= int(s[:-len(fx)]) <= b
    year = lambda s, a, b: len(s) == 4 and s.isdigit() and a <= int(s) <= b
    expected = {
        'byr': lambda s: year(s, 1920, 2002),
        'iyr': lambda s: year(s, 2010, 2020),
        'eyr': lambda s: year(s, 2020, 2030),
        'hgt': lambda s: height(s, 150, 193, 'cm') or height(s, 59, 76, 'in'),
        'hcl': lambda s: rx_color.match(s) is not None,
        'ecl': lambda s: s in colors,
        'pid': lambda s: len(s) == 9 and s.isdigit(),
    }
    def valid(s):
        fields = dict(x.split(':') for x in s.split())
        return all(f(fields.get(k,'')) for k, f in expected.items())
    return sum(map(valid, data.split('\n\n')))


data = '''
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
'''.strip()
assert part1(data) == 2
assert part2(data) == 2

data = open('day4.in').read()
print(part1(data))
print(part2(data))
