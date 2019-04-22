#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys

n, m = map(int, input().split())
x_list = list(map(int, input().split()))
x_list.sort()
gap_list = []
ans = 0

if n >= m:
    print(ans)
    sys.exit(0)
elif n < m:
    for i in range(1, len(x_list)):
        gap_list.append(abs(x_list[i - 1] - x_list[i]))

    gap_list.sort()
    ans = sum(gap_list[0:m - n])

print(ans)
