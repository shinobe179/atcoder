#!/home/shino/.anyenv/envs/pyenv/shims/python

n,a,b = map(int, input().split())
max_ans = 0
min_ans = 0
bigger_num = max([a, b])
smaller_num = min([a, b])

if n - bigger_num >= smaller_num:
    min_ans  = 0
else:
    min_ans = abs(smaller_num - (n - bigger_num))

max_ans = smaller_num

print(max_ans, min_ans)
