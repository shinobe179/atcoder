#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n=int(input())
h=n//3600
m=(n-3600*h)//60
s=n-(3600*h+60*m)
print('{:02}:{:02}:{:02}'.format(h, m, s))
