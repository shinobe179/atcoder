#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys

s = input()
ans = 0

for i in range(1,len(s)):
    if s[0] == "0":
        if i % 2 != 0:
            if s[i] != "1":
                ans += 1
        else:
            if s[i] != "0":
                ans += 1
    elif s[0] == "1":
        if i % 2 != 0:
            if s[i] != "0":
                ans += 1
        else:
            if s[i] != "1":
                ans += 1

print(ans)
