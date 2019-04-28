#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n = int(input())
s_list = [input() for i in range(n)]
s_cntr = Counter(s_list)
m = int(input())
t_list = [input() for i in range(m)]
t_cntr = Counter(t_list)
ans = 0


for k in dict(s_cntr).keys():
    if k in dict(t_cntr).keys():
        tmp = s_cntr[k] - t_cntr[k]
    else:
        tmp = s_cntr[k]
    if ans < tmp:
        ans = tmp

print(ans)
