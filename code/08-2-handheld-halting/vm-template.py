#!/usr/bin/env python
import aocpaiv as aoc
import re
import readline
from collections import deque


class State:
    def __init__(self, program):
        self.program = list(program)
        self.ip = 0
        self.acc = 0
        self.stack = list()


def run_program(state, stdin=None):
    program = state.program
    acc = state.acc
    ip = state.ip
    stack = state.stack
    if not isinstance(stdin, deque):
        stdin = deque(stdin or [])
    stdout = deque()

    def op_nop(x):
        nonlocal ip
        ip += 1

    def op_acc(x):
        nonlocal ip, acc
        acc += x
        ip += 1

    def op_jmp(x):
        nonlocal ip
        ip += x

    def op_mul(x):
        nonlocal ip, acc
        acc *= x
        ip += 1

    def op_jz(x):
        nonlocal ip, acc
        ip += (x if acc == 0 else 1)

    def op_push(x):
        nonlocal ip
        stack.append(x)
        ip += 1

    def op_pop(x):
        nonlocal ip, acc
        acc = stack.pop()
        ip += 1

    def op_out(x):
        nonlocal ip, acc
        stdout.append(acc)
        ip += 1

    def op_in(x):
        nonlocal ip, acc
        if stdin:
            acc = stdin.popleft()
        else:
            acc = int(input('> '))
        ip += 1

    opcodes = {
        'nop': op_nop,
        'acc': op_acc,
        'jmp': op_jmp,
        'mul': op_mul,
        'jz': op_jz,
        'push': op_push,
        'pop': op_pop,
        'out': op_out,
        'in': op_in,
    }

    seen = set()
    while 0 <= ip < len(program):
        if ip in seen: return
        seen.add(ip)

        op, x = program[ip]
        opcodes[op](x)

    state.ip = ip
    state.acc = acc
    state.stack = stack
    return acc


def solve(text):
    # program = [(n, int(x)) for s in text.strip().splitlines() for n,x in [s.split()]]
    program = [(n, int(x)) for n, x in re.findall(r'([a-z]+)\s+([\+\-]\d+)', text)]
    aoc.trace(program)

    state = State(program)
    acc = run_program(state)
    return acc


def test():
    aoc.test_subject(solve)
    aoc.test("""
acc +8
""") == 8


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
