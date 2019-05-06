#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n = int(input())
a,b = map(int, input().split())
k = int(input())
p_array = list(map(int, input().split()))
p_array.append(a)
p_array.append(b)
p_cnt = Counter(p_array)

for i in p_cnt.values():
    if i != 1:
        print('NO')
        sys.exit()

print('YES')
