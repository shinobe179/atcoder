#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys

n = int(input())
s = input()
ans = 0

for i in range(1, len(s)):
    x_set = set(s[0:i])
    y_set = set(s[i::])
    xy_insect = x_set & y_set
    if len(xy_insect) and ans < len(xy_insect):
        ans = len(xy_insect)

print(ans)
