#!/home/shino/.anyenv/envs/pyenv/shims/python

import sys

count = 0
base_index = 0

n, m = map(int, input().split())
a_list = []
for i in range(n):
    a_list.append(input())

b_list = []
for i in range(m):
    b_list.append(input())

for i in range(len(a_list)):
    for j in range(len(b_list)):
        if base_index != 0:
            b_list[j] 
        if b_list[j] in a_list[i]:
            base_index = a_list[i].index(b_list[j])
            count += 1
        if count == m:
            print("Yes")
            sys.exit()

print("No")
sys.exit()
