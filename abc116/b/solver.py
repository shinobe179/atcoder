#!/home/shino/.anyenv/envs/pyenv/shims/python

s = int(input())
a_list = [s]

for i in range(2, 1000000):
    if a_list[-1] % 2 != 0:
        tmp = 3 * a_list[-1] + 1
        if tmp in a_list:
            print(i)
            exit()
        else:
            a_list.append(tmp)
    else:
        tmp = a_list[-1] / 2
        if tmp in a_list:
            print(i)
            exit()
        else:
            a_list.append(tmp)
