#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

a, b, c = map(int, input().split())
m = 10 ** 9 + 7

print(a*b%m*c%m)
