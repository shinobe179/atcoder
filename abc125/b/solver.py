#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n = int(input())
v_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))
t_list = []
ans = 0

for i in range(n):
    t_list.append(v_list[i] - c_list[i])

for i in t_list:
    if i < 0:
        continue
    ans += i

print(ans)

