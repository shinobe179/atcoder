#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter
import math

n = int(input())
pow = 1
m = 10 ** 9 + 7

print(math.factorial(n) % m)
