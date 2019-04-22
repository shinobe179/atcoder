#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys

n = int(input())
l_list = list(map(int, input().split()))


longest_index = l_list.index(max(l_list))
other_sum = 0

for i in range(n):
    if i == longest_index:
        continue
    else:
        other_sum += l_list[i]

if l_list[longest_index] < other_sum:
    print("Yes")
else:
    print("No")
