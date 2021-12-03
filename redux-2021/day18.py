#!/usr/bin/env python
import re


def part1(data):
    def eval(s):
        stack = ['$', '$']
        def reduce():
            c, b, a = stack[-3:]
            if a == ')':
                stack[-3:] = [b]
                return True
            elif isinstance(a, int):
                if b == '+':
                    stack[-3:] = [c + a]
                elif b == '*':
                    stack[-3:] = [c * a]
        for m in re.finditer(r'[+*()]|\d+', s):
            tok = m[0]
            if tok.isdigit():
                tok = int(tok)
            stack.append(tok)
            while reduce(): pass
        return stack[-1]
    ans = sum(map(eval, data.splitlines()))
    return ans


assert part1('1') == 1
assert part1('42') == 42
assert part1('(42)') == 42
assert part1('20 + 22') == 42
assert part1('21 * 2') == 42
assert part1('12 + 9 * 2') == 42
assert part1('2 * 10 + 22') == 42


def part2(data):
    def eval(s):
        # print(s)
        stack = ['$', '$', '$']
        def reduce():
            d, c, b, a = stack[-4:]
            if a == ')':
                if c == '(':
                    stack[-3:] = [b]
                    return True
                elif c == '*':
                    stack[-4:-1] = [d * b]
                    return True
            elif b == '+' and isinstance(a, int):
                stack[-3:] = [c + a]
            elif a == '.':
                if c == '*':
                    stack[-4:-1] = [d * b]
                    return True
        for m in re.finditer(r'[+*().]|\d+', s + '.'):
            tok = m[0]
            if tok.isdigit():
                tok = int(tok)
            stack.append(tok)
            # print(tok, stack)
            while reduce():
                # print(' ', stack)
                pass
        return stack[-2]
    ans = sum(map(eval, data.splitlines()))
    return ans


assert part2('1') == 1
assert part2('42') == 42
assert part2('(42)') == 42
assert part2('20 + 22') == 42
assert part2('21 * 2') == 42
assert part2('12 + 9 * 2') == 42
assert part2('2 * 9 + 12') == 42
assert part2('2 * 10 + 22') == 64
assert part2('7 * 3 * 2') == 42
assert part2('1 + 2 * 3 + 4 * 5 + 6') == 231
assert part2('1 + (2 * 3) + (4 * (5 + 6))') == 51
assert part2('2 * 3 + (4 * 5)') == 46
assert part2('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 1445
assert part2('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 669060
assert part2('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 23340


data = '''
1 + 2 * 3 + 4 * 5 + 6
1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
'''.strip()
assert part1(data) == 26457
assert part2(data) == 694173


data = open('day18.in').read()
print(part1(data))
print(part2(data))