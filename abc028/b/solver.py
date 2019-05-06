#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

s = input()
s_cnt = Counter(s)
a2f = 'ABCDEF'
ans_array = []

for i in a2f:
    try:
        ans_array.append(str(s_cnt[i]))
    except Indexerror:
        ans_array.append('0')

print(' '.join(ans_array))

