#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

s = input()
ans = s[0]
cnt = 1
for i in range(1, len(s[1:])+1):
    if s[i] != s[i-1]:
        ans += str(cnt) + s[i]
        cnt = 1
    elif s[i] == s[i-1]:
        cnt += 1

print(ans+str(cnt))
