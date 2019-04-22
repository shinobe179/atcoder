#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys

A, B, K = map(int, input().split())
ans = 0
count = 0

for i in range(100):
    if A % (100 - i) == 0 and B % (100 - i) == 0:
        ans = 100 - i
        count += 1
        if count == K:
            print(ans)
            sys.exit()
