#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n, m = map(int, input().split())
ab_list = sorted([list(input().split()) for i in range(m)])
ans_list = []

for i in range(len(ab_list)):
    ans_list.append(ab_list[i][0])
    ans_list.append(ab_list[i][1])

ans_cnt = Counter(ans_list)

for i in range(1, n+1):
    try:
        print(ans_cnt[str(i)])
    except IndexError:
        print(0)
