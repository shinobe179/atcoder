#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

s=input()
t=input()
at='atcoder@'
win='You can win'
lose='You will lose'

if not '@' in s+t and s != t:
    print(lose)
    sys.exit()

for i in range(len(s)):
    if s[i] == '@':
        if not t[i] in at:
            print(lose)
            sys.exit()
    elif t[i] == '@':
        if not s[i] in at:
            print(lose)
            sys.exit()
    elif s[i] != t[i]:
        print(lose)
        sys.exit()

print(win)
