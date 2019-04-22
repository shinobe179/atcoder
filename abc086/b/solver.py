#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys

a, b = input().split()
c = int(str(a+b))

if pow(c, 0.5) % 1 == 0:
    print('Yes')
else:
    print('No')
