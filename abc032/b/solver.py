#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

s = input()
k = int(input())
cand_set = set()

for i in range(0, len(s)-k+1, 1):
    cand_set.add(s[i:i+k])

print(len(cand_set))
