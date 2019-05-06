#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n = int(input())
s_list = [input() for _ in range(n)]
ans_list = ['' for _ in range(n)]
#print(s_list)
#print(ans_list)
for i in range(n):
    for j in range(n-1, -1, -1):
        ans_list[i] = ans_list[i] + s_list[j][i] 
    print(''.join(ans_list[i]))
