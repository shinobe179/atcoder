#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n = int(input())
a_list = [int(input()) for _ in range(n)]
past_set = set()
next_hop = 0
cnt = 0

while True:
    if next_hop in past_set:
        print(-1)
        sys.exit()
    else:
        past_set.add(next_hop)
    if next_hop == 1:
        print(cnt)
        sys.exit()
    else:
        next_hop = a_list[next_hop]-1
        cnt += 1
