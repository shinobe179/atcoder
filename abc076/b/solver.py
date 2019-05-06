#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n = int(input())
k = int(input())
ans = 1

for i in range(n):
    if ans <= k:
        ans = ans * 2
    else:
        ans += k

print(ans)
