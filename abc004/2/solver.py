#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys

c_array = [list(input().split())[::-1] for i in range(4)][::-1]
for i in range(4):
    print(' '.join(c_array[i]))
