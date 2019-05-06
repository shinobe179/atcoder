#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys

n=int(input())
if n < 3:
    print(0)
    sys.exit()
m = 10007
ppa = pa = 0
a = 1
for i in range(n-3):
    ppa,pa,a=pa,a,(ppa+pa+a)%m
print(a)
