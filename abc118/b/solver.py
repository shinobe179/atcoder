#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

N, M = map(int, input().split())
KA_list = []
for i in range(N):
    for j in input().split()[1:]:
        KA_list.append(j)
c = Counter(KA_list)

ans = 0
for k, v in c.items():
    if v == N:
        ans += 1

print(ans)
