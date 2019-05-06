#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

s = input()
n = int(input())
lr_array = [input().split() for _ in range(n)]

for array in lr_array:
    l = int(array[0])
    r = int(array[1])
    part = s[l-1:r][::-1]
    s = s[:l-1]+part+s[r:]

print(s)
