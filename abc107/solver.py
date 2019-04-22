#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys

h, w = map(int, input().split())
# '#'が含まれていない行を除いてリストを作る
a_list = []
for i in range(h):
    row = input()
    if '#' in row:
        a_list.append(list(row))

remove_col_list = []
for j in range(w):
    if len([True for v in a_list if v[j] == '#']) == 0:
        remove_col_list.append(j)
remove_col_list = remove_col_list[::-1]

for j in remove_col_list:
    for i in range(len(a_list)):
        a_list[i].pop(j)

for line in a_list:
    print(''.join(line))
