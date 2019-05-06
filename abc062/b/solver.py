#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

h, w = map(int, input().split())
a_list = [input() for i in range(h)]
a_list.insert(0, '#' * w)
a_list.insert(len(a_list), '#' * w)

for i in range(len(a_list)):
    print('#' + a_list[i] + '#')

