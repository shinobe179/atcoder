#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

a = int(input())
b = int(input())

if a < b:
    print('LESS')
elif a > b:
    print('GREATER')
elif a == b:
    print('EQUAL')
