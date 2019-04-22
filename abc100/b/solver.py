#!/home/shino/.anyenv/envs/pyenv/shims/python

import sys

d, n = map(int, input().split())
ans = 0

if n == 100:    
    print(100 ** d * 101) 
else:
    print(100 ** d * n)
