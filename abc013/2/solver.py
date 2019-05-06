import sys
from collections import Counter
 
a=int(input())
b=int(input())
ans = 10
 
for i in [-1, 1]:
    tmp = a
    cnt = 0
    while str(abs(tmp))[-1] != str(b):
        tmp += i
        cnt += 1
        print(tmp, cnt)
    if cnt < ans:
        ans = cnt

