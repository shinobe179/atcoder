#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys

dish_list = [input() for i in range(5)]
ans = 0

for i in range(len(dish_list)):
    if int(dish_list[i][-1]) == 0:
        dish_list.insert(0, dish_list[i])
        del dish_list[i+1]
        continue
    for j in range(len(dish_list) - 1):
        if int(dish_list[j][-1]) < int(dish_list[j+1][-1]):
            dish_list[j], dish_list[j+1] = dish_list[j+1], dish_list[j]

#print(dish_list)

for i in range(len(dish_list)):
    tmp = int(dish_list[i])
    if i == len(dish_list) - 1 or tmp % 10 == 0:
        ans += tmp
    else:
        ans += tmp
        ans += 10 - tmp % 10

print(ans)
