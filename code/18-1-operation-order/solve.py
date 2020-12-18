#!/usr/bin/env python
import aocpaiv as aoc
import re


def solve(text):
    def eval(text):
        stack = list()

        opcodes = {
            '+': int.__add__,
            '*': int.__mul__,
        }

        def reduce():
            if len(stack) > 2:
                c, b, a = stack[-3:]
                if isinstance(a, int) and stack[-2] in '+*':
                    stack[-3:] = [opcodes[b](c, a)]
                    return True
                elif a == ')' and c == '(':
                    stack[-3:] = [b]
                    return True
            return False

        for num, token in re.findall(r'(\d+)|([+*()])', text):
            if num: token = int(num)
            stack.append(token)
            while reduce(): pass
        return stack[-1]

    return sum(map(eval, text.splitlines()))


def test():
    aoc.test_subject(solve)
    aoc.test('1 + 2 * 3 + 4 * 5 + 6') == 71
    aoc.test('2 * 3 + (4 * 5)') == 26
    aoc.test('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 437
    aoc.test('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 12240
    aoc.test('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 13632


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
