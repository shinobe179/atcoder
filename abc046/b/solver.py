#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n, k = map(int, input().split())

print(k * ((k-1) ** (n-1)))
