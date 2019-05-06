#!/home/shino/.anyenv/envs/pyenv/shims/python

n=int(input())
a_array=[int(v) for v in input().split()]
ans=0

for v in a_array:
    tmp = v
    while tmp % 2 == 0 or tmp % 5 == 0:
        ans+=1
        tmp-=1

print(ans)
