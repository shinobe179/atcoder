#!/home/shino/.anyenv/envs/pyenv/shims/python

n = int(input())
p_list = [int(input()) for i in range(n)]
max_p = max(p_list)
max_p_index = p_list.index(max_p)
ans = 0

for i in range(n):
    if i == max_p_index:
        ans += p_list[i] // 2
    else:
        ans += p_list[i]

print(ans)
