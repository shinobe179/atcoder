#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

x, y, z = map(int, input().split())
x = x - z
print(str(x // (y + z)))
