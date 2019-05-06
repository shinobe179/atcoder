#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

s = input()
ans = ''

for i in s:
    if i == 'B':
        ans = ans[:-1]
    else:
        ans = ans + i

print(ans)

