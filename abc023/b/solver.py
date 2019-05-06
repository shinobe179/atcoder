#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n = int(input())
s = input()
if s == 'b':
    print(0)
    sys.exit()
ss = 'b'
cnt = 1

while len(ss) <= len(s):
    if cnt % 3 == 0:
        ss = 'b' + ss + 'b'
    elif cnt % 3 == 1:
        ss = 'a' + ss + 'c'
    elif cnt % 3 == 2:
        ss = 'c' + ss + 'a'
    if s == ss:
        print(cnt)
        sys.exit()
    cnt += 1
print(-1)
