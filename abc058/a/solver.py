#!/home/shino/.anyenv/envs/pyenv/shims/python

a, b, c = map(int, input().split())

if b - a == c - b:
    print("YES")
else:
    print("NO")
