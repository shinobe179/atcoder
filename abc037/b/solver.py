#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n, q = map(int, input().split())
ans_list = [0 for i in range(n)]
lrt_list = [list(map(int, input().split())) for _ in range(q)]

for i in lrt_list:
    for j in range(i[0]-1, i[1]):
        ans_list[j] = i[2]

for i in ans_list:
    print(i)
