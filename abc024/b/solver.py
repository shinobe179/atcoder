#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n,t = map(int, input().split())
a_array = [int(input()) for _ in range(n)]
ans = t

for i in range(len(a_array)-1):
    if a_array[i]+t < a_array[i+1]:
        ans += t
    else:
        ans += a_array[i+1]-a_array[i]

print(ans)
