#!/usr/bin/env python
import sys
from collections import defaultdict


def main(fn='input.txt'):
    with open(fn) as fp:
        text = fp.read()

    grid = {(y, x):1
        for y,s in enumerate(text.strip().splitlines())
        for x,v in enumerate(s)
        if v == 'L'}
    w = max(x for _,x in grid.keys()) + 1
    h = max(y for y,_ in grid.keys()) + 1

    # print('width =', w)
    # print('height =', h)
    data = [[sum((grid.get((y,x),0) << (15-i)) for i,x in enumerate(range(col, col+16))) for col in range(0, (w+15)//16*16, 16)] for y in range(h)]
    def atos(xs):
        return '{{{}}}'.format(','.join(map(str, xs)))
    data = atos(map(atos, data))
    print(f'data = {data}')


if __name__ == '__main__':
    main(*sys.argv[1:])
