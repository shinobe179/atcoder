#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n = int(input())
d, x = map(int, input().split())
a_list = [int(input()) for _ in range(n)]
ans = x

for i in a_list:
    ans += d // i
    if d % i != 0:
        ans += 1
print(ans)
