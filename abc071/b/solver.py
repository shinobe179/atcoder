#!/home/shino/.anyenv/envs/pyenv/shims/python
import string
import sys
from collections import Counter

s = input()
all = string.ascii_lowercase
rest = list(set(all) - set(s))

if len(rest) == 0:
    print('None')
else:
    print(sorted(rest)[0])
