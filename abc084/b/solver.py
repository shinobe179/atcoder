#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

a, b = map(int, input().split())
s = input()

for i in range(len(s)):
    if i <= a-1:
        if not s[i].isdigit():
            print('No')
            sys.exit()
    elif i == a:
        if not s[i] == '-':
            print('No')
            sys.exit()
    elif i <= a + b + 1:
        if not s[i].isdigit():
            print('No')
            sys.exit()
    else:
        print('No')
        sys.exit()

print('Yes')
