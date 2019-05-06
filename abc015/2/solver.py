#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n=int(input())
a_array=[float(i) for i in input().split() if int(i) != 0]
ans=sum(a_array)/len(a_array)
print(int(ans) if ans%1==0 else int(1+sum(a_array)//len(a_array)))
