#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

x = int(input())
ans = 0

for i in range(1, 35):
    for j in range(2, 35):
        if ans < i ** j <= x:
            ans = i ** j

print(ans)
