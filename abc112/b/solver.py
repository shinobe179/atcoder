#!/home/shino/.anyenv/envs/pyenv/shims/python

n, t = map(int, input().split())
ct_list = [tuple(map(int, input().split())) for i in range(n)]
ans = 1001

for i in ct_list:
    if i[1] > t:
        continue
    if ans > i[0]:
        ans = i[0]

if ans < 1001:
    print(ans)
else:
    print("TLE")
