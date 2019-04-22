#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys

A, B, C = map(int, input().split())
D = B // A

if C <= D:
    print(C)
else:
    print(D)
