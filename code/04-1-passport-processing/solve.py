#!/usr/bin/env python
import aocpaiv as aoc


def solve(text):
    expect = set('byr iyr eyr hgt hcl ecl pid cid'.split())
    def valid(batch):
        batch = dict(p.split(':') for p in batch.split())
        if (set(batch) | {'cid'}) & expect != expect:
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
