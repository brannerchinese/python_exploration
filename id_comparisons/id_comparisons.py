#!/usr/bin/python
# id_comparisons.py
# David Prager Branner
# 20140219

import array

items = [[1, 2, 3],
        '123',
        (1, 2, 3),
        array.array("i", [1, 2, 3]),
        bytes(123)
        ]
bases = [('list', '[1, 2, 3]'), 
        ('string', '"123"'), 
        ('tuple', '(1, 2, 3)'), 
        ('array', 'array.array("i", [1, 2, 3])'), 
        ('byte', 'bytes(123)')]
cases = [
        'eval(base) == eval(base)',
        'eval(base) == eval(base)[:]',
        'id(eval(base)) == id(eval(base))',
        'id(eval(base)) == id(eval(base)[:])',
        'id(eval(base)[:]) == id(eval(base)[:])',
#        'x == x[:]',
        'id(x) == id(x[:])',
        'id(x[:]) == id(x)',
        'id(x[:]) == id(x[:])',
        'id(x) == id(eval(base))',
        'id(eval(base)) == id(x)',
        'id(x[:]) == id(eval(base))',
        'id(x[:]) == id(eval(base)[:])',
        'id(x) == id(y)',
        'id(x[:]) == id(y[:])',
        'id(y) == id(eval(base))',
        ]
raw_cases = [
        '[1, 2, 3] == [1, 2, 3]',
        '[1, 2, 3] == [1, 2, 3][:]',
        'id([1, 2, 3]) == id([1, 2, 3])',
        'id([1, 2, 3]) == id([1, 2, 3][:])',
        'id([1, 2, 3][:]) == id([1, 2, 3][:])',
#        'x == x[:]',
        'id(x) == id(x[:])',
        'id(x[:]) == id(x)',
        'id(x[:]) == id(x[:])',
        'id(x) == id([1, 2, 3])',
        'id([1, 2, 3]) == id(x)',
        'id(x[:]) == id([1, 2, 3])',
        'id(x[:]) == id([1, 2, 3][:])',
        'id(x) == id(y)',
        'id(x[:]) == id(y[:])',
        'id(y) == id([1, 2, 3])'
        ]

def main():
    for base in bases:
        print('\n', base[0])
        base = base[1]
        x = eval(base)
        y = x[:]
        for case in cases:
            print(case, eval(case))
    print('\nRaw lists')
    x = [1, 2, 3]
    y = x[:]
    for case in raw_cases:
        print(case, eval(case))

    return x, y

if __name__ == '__main__':
    main()