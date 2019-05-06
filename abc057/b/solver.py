#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n, m = map(int, input().split())
ab_list = [ list(map(int, input().split())) for i in range(n)]
cd_list = [ list(map(int, input().split())) for i in range(m)]
ans_list = [[None, None] for i in range(n)]

for i in range(n):
    for j in range(m):
        x_dist = abs(ab_list[i][0] - cd_list[j][0])
        y_dist = abs(ab_list[i][1] - cd_list[j][1])
        tmp = x_dist + y_dist
        if ans_list[i][0] == None or tmp < ans_list[i][1]:
            ans_list[i] = [j+1, tmp]

for i in range(n):
    print(ans_list[i][0])
