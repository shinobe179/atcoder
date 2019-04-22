#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys

abc_list = []
for i in range(5):
    abc_list.append(int(input()))

k = int(input())

for i in range(0, len(abc_list)):
    for j in range(0, len(abc_list)):
        if i == j:
            continue
        if abs(abc_list[i] - abc_list[j]) > k:
            print(':(')
            sys.exit()

print('Yay!')
