#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n = int(input())
k = int(input())
x_list = list(map(int, input().split()))
ans = 0

for i in x_list:
    if k - i < i:
        ans += (k - i) * 2
    else:
        ans += i * 2

print(ans)
