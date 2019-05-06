#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n = int(input())
a_array = [int(input()) for i in range(n)]
a_dict = {}
ans = 0

for i in range(len(a_array)):
    try:
        if a_dict[a_array[i]] == True:
            ans += 1
    except:
        a_dict[a_array[i]] = True

print(ans)
