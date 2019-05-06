#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n = int(input())
sp_array = [input().split() for _ in range(n)]
sp_dict = {s:int(p) for s,p in sp_array}
pop = sum(sp_dict.values())

for s,p in sp_dict.items():
    if p > pop // 2:
        print(s)
        sys.exit()

print('atcoder')
