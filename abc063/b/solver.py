#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

s_cnt = Counter(input())

for i in s_cnt.values():
    if i != 1:
        print('no')
        sys.exit()

print('yes')
