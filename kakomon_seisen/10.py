#!/home/shino/.pyenv/shims/python

n = int(input())
for i in range(n):
    t, x, y = map(int, input().split())
    if x + y > t or ((x + y) % 2 != t % 2):
        print("No")
        exit()
print("Yes")    
