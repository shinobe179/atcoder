#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

a, b, c, d = map(int, input().split())

ans = min(b, d) - max(a, c)

if ans < 0:
    ans = 0

print(ans)
