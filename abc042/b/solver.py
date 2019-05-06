#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n, l = map(int, input().split())
s_list = sorted([input() for _ in range(n)])

print(''.join(s_list))
