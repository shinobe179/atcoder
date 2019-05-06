#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

o = input()
e = input()
ans = []

for i in range(len(o)):
    ans.append(o[i])
    try:
        ans.append(e[i])
    except IndexError:
        pass

print(''.join(ans))
