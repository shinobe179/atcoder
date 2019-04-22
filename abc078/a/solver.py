#!/home/shino/.anyenv/envs/pyenv/shims/python

x,y = input().split()

x = int(ord(x)) 
y = int(ord(y)) 

if x > y:
    print(">")
elif x == y:
    print("=") 
else:
    print("<")
