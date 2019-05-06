#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n = int(input())
ans = 10 ** 10

for i in range(1, n+1):
    b = n//i
    tmp = abs(i-b) + n-i*b
    ans = min(ans, tmp)

print(ans)
