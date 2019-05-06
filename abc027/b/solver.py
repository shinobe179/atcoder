#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

n = int(input())
a_array = list(map(int, input().split()))
avg = sum(a_array) / n
brg_array = [0 for i in range(n-1)]

if avg % 1 != 0:
    print(-1)
    sys.exit()

if sum(a_array[1:]) != avg*len(a_array[1:]):
    brg_array[0] = 1

for i in range(1, len(a_array)):
    if sum(a_array[:i]) != avg*len(a_array[:i]):
            brg_array[i-1] = 1
    if sum(a_array[i+1:]) != avg*len(a_array[i+1:]):
            brg_array[i] = 1
       
print(sum(brg_array))
