#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n, m = map(int, input().split())

if n == 12:
    n = 0
elif n > 12:
    n %= 12

na = n*30+m*0.5
ma = m*6
print(min(abs(na-ma), 360-abs(ma-na)))
