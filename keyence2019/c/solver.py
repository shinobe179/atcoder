#!/home/shino/.anyenv/envs/pyenv/shims/python

n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
supply_list = []
lack = 0
lack_cnt = 0

for i in range(n):
    if a_list[i] < b_list[i]:
        lack += b_list[i] - a_list[i]
        lack_cnt += 1
    elif a_list[i] > b_list[i]:
        supply_list.append(a_list[i] - b_list[i])

if lack_cnt == 0:
    print(0)
    exit()
elif len(supply_list) == 0:
    print(-1)
    exit()

supply = 0
supply_cnt = 0

for i in sorted(supply_list, reverse=True):
    supply += i
    supply_cnt += 1
    if supply >= lack:
        break

if supply < lack:
    print(-1)
    exit()

print(lack_cnt + supply_cnt)
