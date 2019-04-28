#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys

n = int(input())
a_list = list(map(int, input().split()))

print(sorted(a_list)[-1] - sorted(a_list)[0])
