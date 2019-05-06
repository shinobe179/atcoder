#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n, k = map(int, input().split())
l_array = sorted(list(map(int, input().split())), reverse=True)

print(sum(l_array[:k]))
