#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys

n, x = map(int, input().split())
a_array = [int(v) for v in input().split()]
ans = 0
for i in range(n):
    if x&(1<<i):
        ans += a_array[i]

print(ans)
