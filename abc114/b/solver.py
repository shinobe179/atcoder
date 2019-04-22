#!/home/shino/.anyenv/envs/pyenv/shims/python

s = input()
ans = 753

for i in range(len(s)):
    x = int(s[i:i+3])
    if len(str(x)) > 3:
        break
    x = abs(x - 753)
    if x < ans:
        ans = x

print(ans)
