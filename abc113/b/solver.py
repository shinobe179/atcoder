#!/home/shino/.anyenv/envs/pyenv/shims/python

n = int(input())
t, a = map(int, input().split())
h_list = list(map(int, input().split()))
ans = 1000
ansi = 0

for ix, x in enumerate(h_list):
    tmp = t - x * 0.006
    if ans > abs(a - tmp):
        ans = abs(a - tmp)
        ansi = ix + 1
print(ansi)
