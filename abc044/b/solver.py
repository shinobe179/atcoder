#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

w = input()
w_cnt = Counter(w)

for i in w_cnt.values():
    if i % 2 != 0:
        print('No')
        sys.exit()

print('Yes')
