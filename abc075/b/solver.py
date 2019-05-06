#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

h, w = map(int, input().split())
s_list = [list('.' * (w + 2))]
s_list.extend([list('.' + input() + '.') for i in range(h)])
s_list.append(list('.' * (w + 2)))

for i in range(1, h+1):
    for j in range(1, w+1):
        if s_list[i][j] == '.':
            cnt = 0
            cnt += s_list[i-1][j-1:j+2].count('#')
            cnt += s_list[i][j-1:j+2].count('#')
            cnt += s_list[i+1][j-1:j+2].count('#')
            s_list[i][j] = str(cnt)

for i in s_list[1:-1]:
    print(''.join(i[1:-1]))
