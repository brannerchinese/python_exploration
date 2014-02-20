#!/usr/bin/python
# id_seq_length.py
# David Prager Branner
# 20140220

"""Answer the question: does sequence length affect the behavior of `id()`?"""

import random

def main():
    # List
    #
    # String
    for trial in range(6):
        length = 10 ** trial
        liszt = [str(random.randint(0, 9)) for i in range(length)]
        liszt_slice = liszt[:]
        sztring = ''.join(liszt)
        sztring_slice = sztring[:]
        thuple = tuple(liszt)
        thuple_slice = thuple[:]
        print('\n*******\n')
        print(trial, 'id(liszt) == id(liszt[:])', 
                id(liszt) == id(liszt[:]))
        print(trial, 'id(liszt[:]) == id(liszt[:][:])', 
                id(liszt[:]) == id(liszt[:][:]))
        print(trial, 'id(liszt) == id(liszt_slice)', 
                id(liszt) == id(liszt_slice))
        print('\n')
        print(trial, 'id(sztring) == id(sztring[:])', 
                id(sztring) == id(sztring[:]))
        print(trial, 'id(sztring[:]) == id(sztring[:][:])', 
                id(sztring[:]) == id(sztring[:][:]))
        print(trial, 'id(sztring) == id(sztring_slice)', 
                id(sztring) == id(sztring_slice))
        print('\n')
        print(trial, 'id(thuple) == id(thuple[:])', 
                id(thuple) == id(thuple[:]))
        print(trial, 'id(thuple[:]) == id(thuple[:][:])', 
                id(thuple[:]) == id(thuple[:][:]))
        print(trial, 'id(thuple) == id(thuple_slice)', 
                id(thuple) == id(thuple_slice))


if __name__ == '__main__':
    main()