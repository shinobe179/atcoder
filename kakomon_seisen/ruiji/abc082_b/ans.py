#!/home/shino/.pyenv/shims/python
s = sorted(input().encode("utf-8"))
t = sorted(input().encode("utf-8"))
print(s, t)
if s < t:
    print('Yes')
    exit()
print('No')
