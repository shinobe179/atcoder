#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

a, b, k = map(int, input().split())
ans_set = set()

for i in range(a, a+k):
    if i > b:
        break
    ans_set.add(i)

for i in range(b, b-k, -1):
    if i in ans_set or b-k < 0:
        break
    ans_set.add(i)

for i in sorted(ans_set):
    print(i)
