#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys

S = input()
acgt = 'ACGT'
ans = 0

for i in range(len(S)):
    tmp = 0
    for j in range(i, len(S)):
        if S[j] in acgt:
            tmp += 1
        else:
            break
    if tmp > ans:
        ans = tmp

print(ans)
