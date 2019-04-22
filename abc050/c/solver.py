#!/home/shino/.anyenv/envs/pyenv/shims/python

n = int(input())
a = [int(i) for i in input().split()]
 
a_dict = {}
for v in a:
    if v in a_dict:
        a_dict[v] += 1
    else:
        a_dict[v] = 1
 
 
if n % 2 == 0:
    possible_list = [i for i in range(1, n, 2)]
    for k, v in a_dict.items():
        if v != 2 or k not in possible_list:
            print(0)
            exit()
else:
    possible_list = [i for i in range(0, n, 2)]
    if a_dict[0] != 1:
        print(0)
        exit()
    else:
        a_dict[0] = 2
        for k, v in a_dict.items():
            if v != 2 or k not in possible_list:
                print(0)
                exit()
 
print(2 ** (n // 2) % (10 ** 9 + 7))
