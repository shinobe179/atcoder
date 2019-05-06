#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n = int(input())
if n == 0:
    print(2)
    sys.exit()
elif n == 1:
    print(1)
    sys.exit()
l_list = [2, 1]
i = 2

while True:
    l_list.append(l_list[i-1] + l_list[i-2])
    if len(l_list) - 1 == n:
        print(l_list[-1])
        sys.exit()
    i += 1
