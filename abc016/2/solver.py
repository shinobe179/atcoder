#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

a,b,c = map(int, input().split())
ans_dict = {'p':False, 'm':False}

if a+b==c:
    ans_dict['p'] = True
if a-b==c:
    ans_dict['m'] = True

if ans_dict['p']==True and ans_dict['m']== True:
    print('?')
elif ans_dict['p']==True:
    print('+')
elif ans_dict['m']==True:
    print('-')
else:
    print('!')

