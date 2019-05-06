#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n, a, b = map(int, input().split())
ans = 0

for _ in range(n):
    tmp_array = input().split()
    direction = tmp_array[0]
    distance = int(tmp_array[1])
    if distance < a:
        distance = a
    elif distance > b:
        distance = b
    if direction == 'West':
        distance *= -1

    ans += distance

if ans == 0:
    print(0)
elif ans < 0:
    print('West', abs(ans))
else:
    print('East', ans)
