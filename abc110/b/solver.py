#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys

n, m, x, y = map(int, input().split())
x_list = list(map(int, input().split()))
y_list = list(map(int, input().split()))

for z in range(x + 1, y + 1):
    if max(x_list) < z:
        if min(y_list) >= z:
            print("No War")
            sys.exit(0)

print("War")
