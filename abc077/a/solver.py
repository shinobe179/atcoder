#!/home/shino/.anyenv/envs/pyenv/shims/python

upper = input()
lower = input()

rev_lower = ('').join([i for i in lower[::-1] ])

if upper == rev_lower:
    print("YES")
else:
    print("NO")
