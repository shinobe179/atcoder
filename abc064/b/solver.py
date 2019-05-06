#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n = int(input())
a_list = sorted(list(set(list(map(int, input().split())))))
ans = 0

for i in range(1, len(a_list)):
    ans += a_list[i] - a_list[i-1]

print(ans)
