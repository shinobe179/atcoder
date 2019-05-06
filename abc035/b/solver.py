#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

x, y = 0, 0
s = input()
t = int(input())
q = s.count('?')
s = s.replace('?', '')

for i in s:
    if i == 'L':
        x -= 1
    elif i == 'R':
        x += 1
    elif i == 'U':
        y += 1
    elif i == 'D':
        y -= 1

ans = abs(x) + abs(y)

if t == 2:
    q = q * -1

ans = ans + q

if ans < 0:
    ans %= 2

print(ans)
