#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys

N, M, C = map(int, input().split())
b_list = list(map(int, input().split()))
a_list = [ list(map(int, input().split())) for i in range(N) ]

#print(N, M, C, b_list, a_list)

ans = 0

for i in range(len(a_list)):
    tmp = 0
    for j in range(len(a_list[i])):
        tmp += a_list[i][j] * b_list[j]
    if tmp + C > 0:
        ans += 1

print(ans)
