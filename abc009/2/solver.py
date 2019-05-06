#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n=int(input())
a_array=[int(input()) for a in range(n)]
a_set=set(a_array)
a_sorted_array=sorted(list(a_set))
print(a_sorted_array[-2])
