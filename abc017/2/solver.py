#!/home/shino/.anyenv/envs/pyenv/shims/python
import re
import sys
from collections import Counter

s = re.sub(r'(ch|o|k|u)', '', input())
if len(s) == 0:
    print('YES')
else:
    print('NO')
