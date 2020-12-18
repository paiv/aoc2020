#!/usr/bin/env python
import aocpaiv as aoc
import re


def solve(text):
    def eval(text):
        stack = list()

        def reduce():
            if len(stack) > 2:
                c, b, a = stack[-3:]
                if isinstance(a, int) and b == '+':
                    stack[-3:] = [c + a]
                    return True
                elif a == ')' and c == '(':
                    stack[-3:] = [b]
                    return True
                elif (a == ')' or a == '.') and c == '*':
                    x = stack[-4]
                    stack[-4:-1] = [x * b]
                    return True
            elif stack[-1] == '.' and len(stack) == 2:
                stack[-2:] = [stack[-2]]
                return True
            return False

        for num, token in re.findall(r'(\d+)|([+*().])', text + '.'):
            if num: token = int(num)
            stack.append(token)
            while reduce(): pass
        return stack[-1]

    return sum(map(eval, text.splitlines()))


def test():
    aoc.test_subject(solve)
    aoc.test('1 + 2 * 3 + 4 * 5 + 6') == 231
    aoc.test('1 + (2 * 3) + (4 * (5 + 6))') == 51
    aoc.test('2 * 3 + (4 * 5)') == 46
    aoc.test('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 1445
    aoc.test('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 669060
    aoc.test('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 23340


if __name__ == '__main__':
    test()
    print(solve(aoc.read_files()))
