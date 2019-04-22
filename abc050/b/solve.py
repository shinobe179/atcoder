#!/home/shino/.anyenv/envs/pyenv/shims/python

n = int(input())
t_list = list(map(int, input().split()))
m = int(input())
for i in range(m):
    tmp_list = list(map(int, input().split()))
    print(sum(t_list) - t_list[tmp_list[0] - 1] + tmp_list[1])
