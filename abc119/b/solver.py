#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys

N = int(input())
xu_list = [input().split() for i in range(N)]

#print(N, xu_list)
ans = 0

for i in xu_list:
    if i[1] == 'BTC':
        ans += float(i[0]) * 380000
    else:
        ans += float(i[0])

print(ans)
