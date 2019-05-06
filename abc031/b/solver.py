#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

l, h = map(int, input().split())
n = int(input())
a_list = [int(input()) for _ in range(n)]

for t in a_list:
    if t < l:
        print(l-t)
    elif l <= t <= h:
        print(0)
    elif h < t:
        print(-1)
