#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

a, b, c = map(int, input().split())

for i in range(a, b*a+1, a):
    if i % b == c:
        print('YES')
        sys.exit()

print('NO')
