#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter
import math

n = int(input())
r_array = sorted([int(input()) for _ in range(n)], reverse=True)
pi = math.pi
c_array = []
ans = 0

for i in range(len(r_array)):
    if (i + 1) % 2 != 0:
        ans += r_array[i]**2
    else:
        ans -= r_array[i]**2
print(ans*pi)
