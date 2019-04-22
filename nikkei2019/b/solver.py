#!/home/shino/.anyenv/envs/pyenv/shims/python

n = int(input())
abc_list = []
for i in range(3):
    abc_list.append(input())
ans = 0
diff = 0

for i in range(n):
    if abc_list[0][i] != abc_list[1][i]:
        diff += 1
    if abc_list[0][i] != abc_list[2][i]:
        diff += 1

    if diff == 0:
        pass
    elif diff == 1:
        ans += 1
    elif diff == 2 and abc_list[1][i] == abc_list[2][i]:
        ans += 1
    else:
        ans += 2
    diff = 0

print(ans)
