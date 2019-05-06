#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

s = input()

for i in range(1, len(s)):
    ts = s[:-i]
    if len(ts) % 2 != 0:
        continue
    #print(len(ts), ts, s[:len(ts)//2], s[len(ts)//2:])
    if ts[:len(ts)//2] == ts[len(ts)//2:]:
        print(len(ts))
        sys.exit()
