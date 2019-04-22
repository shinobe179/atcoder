#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from datetime import datetime

S = input()
s_date = datetime.strptime(S, '%Y/%m/%d')
last_heisei = datetime.strptime('2019/04/30', '%Y/%m/%d')

if s_date > last_heisei:
    print('TBD')
else:
    print('Heisei')

