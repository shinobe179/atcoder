#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

bw, bh = 0, 0
w, h, n = map(int, input().split())
xya_array = [list(map(int, input().split())) for _ in range(n)]

for i in xya_array:
    if i[2] == 1:
        bw = max(bw, i[0])
    elif i[2] == 2:
        w = min(w, i[0])
    elif i[2] == 3:
        bh = max(bh, i[1])
    elif i[2] == 4:
        h = min(h, i[1])

if w-bw < 0 or h-bh < 0:
    print(0)
else:
    print((w-bw)*(h-bh))
