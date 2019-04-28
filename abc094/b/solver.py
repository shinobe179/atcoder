#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n, m, x = map(int, input().split())
a_list = list(map(int, input().split()))
math_list = []

for i in range(n):
    if i in a_list:
        math_list.append(1)
    else:
        math_list.append(0)
#print(n, x, a_list, math_list)
print(min(sum(math_list[0:x]), sum(math_list[x+1::])))
