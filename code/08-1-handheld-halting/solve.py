#!/usr/bin/env python -OO
import aocpaiv as aoc


def run_program(program):
    acc = 0
    ip = 0
    seen = set()
    while 0 <= ip < len(program):
        if ip in seen: break
        seen.add(ip)
        op, x = program[ip]
        aoc.trace(ip, op, x)

        if op == 'acc':
            acc += x
            ip += 1
        elif op == 'jmp':
            ip += x
        elif op == 'nop':
            ip += 1
    return acc


def solve(text):
    program = [(n, int(x)) for s in text.strip().splitlines() for n,x in [s.split()]]
    aoc.trace(program)
    return run_program(program)


def test():
    aoc.test_subject(solve)
    aoc.test("""
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""") == 5


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
