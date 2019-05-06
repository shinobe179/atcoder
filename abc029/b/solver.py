#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

s_list = [input() for _ in range(12)]
ans = 0
for s in s_list:
    if 'r' in s:
        ans += 1
print(ans)
