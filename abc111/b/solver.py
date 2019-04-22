#!/home/shino/.anyenv/envs/pyenv/shims/python

import sys

n = int(input())

for i in range(n, 1000):
    if str(i)[0] == str(i)[1] == str(i)[2]:
        print(i)
        sys.exit(0)
