#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n = int(input())
hn = 0
for i in str(n):
    hn += int(i)

if n % hn == 0:
    print('Yes')
else:
    print('No')
