#!/usr/bin/env python
import re


def part1(data):
    program = [(m[1], int(m[2])) for m in re.finditer(r'(acc|jmp|nop)\s+([+-]\d+)', data)]
    seen = set()
    ip = reg = 0
    while 0 <= ip < len(program):
        if ip in seen: break
        seen.add(ip)
        op, x = program[ip]
        if op == 'acc':
            reg += x
            ip += 1
        elif op == 'jmp':
            ip += x
        elif op == 'nop':
            ip += 1
    return reg
    

def part2(data):
    program = [(m[1], int(m[2])) for m in re.finditer(r'(acc|jmp|nop)\s+([+-]\d+)', data)]
    patches = [i for i,(op,x) in enumerate(program) if op == 'jmp']
    for patch in reversed(patches):
        seen = set()
        ip = reg = 0
        while 0 <= ip < len(program):
            if ip in seen: break
            seen.add(ip)
            op, x = program[ip]
            if ip == patch or op == 'nop':
                ip += 1
            elif op == 'acc':
                reg += x
                ip += 1
            elif op == 'jmp':
                ip += x
        else:
            # print(f'patch {pi}: {pop[0]} {pop[1]}')
            return reg


data = '''
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
'''.strip()
assert part1(data) == 5
assert part2(data) == 8


data = open('day8.in').read()
print(part1(data))
print(part2(data))
