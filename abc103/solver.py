#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys

s = input()
t = input()

for i in range(len(s)+1):
    if i == 0:
        rs = s
    else:
        rs = str(rs[-1] + rs[0:-1])
    if rs == t:
        print('Yes')
        sys.exit()

print('No')
