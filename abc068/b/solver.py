#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n = int(input())

for i in range(n, 0, -1):
    if i & (i-1) == 0:
        print(i)
        sys.exit()
