#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

m = int(input()) / 1000

if m < 0.1:
    print('00')
    sys.exit()
elif 0.1 <= m <= 5:
    print(str(int(m * 10)).zfill(2))
    sys.exit()
elif 6 <= m <= 30:
    print(str(int(m + 50)))
    sys.exit()
elif 35 <= m <= 70:
    print(str(int((m - 30) / 5 + 80)))
    sys.exit()
elif 70 < m:
    print('89')
    sys.exit()
