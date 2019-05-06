#!/home/shino/.anyenv/envs/pyenv/shims/python
from collections import Counter
n=int(input())
s_array=[input() for a in range(n)]
s_cntr=Counter(s_array)
s_sorted=[k for k,v in sorted(s_cntr.items(), key=lambda x: -x[1])]
print(s_sorted[0])
