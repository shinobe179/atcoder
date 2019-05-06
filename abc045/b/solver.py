#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

sa = input()
sb = input()
sc = input()

turn = 'a'

while True:
    if turn == 'a':
        turn = sa[0]
        sa = sa[1:]
    elif turn == 'b':
        turn = sb[0]
        sb = sb[1:]
    elif turn =='c':
        turn = sc[0]
        sc = sc[1:]
    if len(sa) == 0 and turn == 'a':
        print('A')
        sys.exit()
    elif len(sb) == 0 and turn == 'b':
        print('B')
        sys.exit()
    elif len(sc) == 0 and turn == 'c':
        print('C')
        sys.exit()

