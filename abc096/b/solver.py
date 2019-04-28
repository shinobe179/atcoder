#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

abc_list = list(map(int, input().split()))
k = int(input())

for i in range(k):
    max_index = abc_list.index(max(abc_list))
    abc_list[max_index] = abc_list[max_index] * 2

print(sum(abc_list))
