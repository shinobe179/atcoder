#!/home/shino/.anyenv/envs/pyenv/shims/python

import numpy as np
import sys

n = int(input())
dish_list = []
diff_list = []
each_list = [[],[]]

for i in range(n):
    dish_list.append(list(map(int, input().split())))
    diff_list.append(dish_list[i][0] - dish_list[i][1])
    each_list[0].append(dish_list[i][0])
    each_list[1].append(dish_list[i][1])

# index0 = Aolki, 1 = Takahashi
point_list = [0, 0]

while len(dish_list) != 0:
    for i in range(2):
        if len(dish_list) == 0:
            print(point_list[0] - point_list[1])
            sys.exit()
        # 差値リストが1以上ならまず差を調べる
        custom_dish_list = []
        if sum(diff_list) != 0:
            # 青木君は値が最大の料理を確認する
            if i == 0:
                indexes = [i for i in range(len(diff_list)) if diff_list[i] == max(diff_list)]
            # 高橋君は値が最小の料理を確認する
            elif i == 1:
                indexes = [i for i in range(len(diff_list)) if diff_list[i] == min(diff_list)]
            # その中で、自分が食べた時の幸福度が最大の料理を確認する
            for k in indexes:
                custom_dish_list.append(dish_list[k])
            ate_index = np.argmax(custom_dish_list)
            point_list[i] += max(custom_dish_list[ate_index])    
        # 差がないなら、単純に自分が食べた時の幸福度が最大の料理を確認する
        else:
            ate_index = np.argmax(each_list[i])
            point_list[i] += max(each_list[i])
    
        # 食べた料理の消去
        dish_list.pop(ate_index)      
        diff_list.pop(ate_index)      
        each_list[0].pop(ate_index)      
        each_list[1].pop(ate_index)      

print(point_list[0] - point_list[1])
