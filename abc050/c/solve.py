#!/home/shino/.anyenv/envs/pyenv/shims/python

n = int(input())
a_list = list(map(int, input().split()))

if n == 1:
    print(1)
    exit()

if n % 2 != 0:
    if a_list.count(0) != 1:
        print(0)
        exit()
    else:
        for i in range(2, n, 2):
            if a_list.count(i) != 2:
                print(0)
                exit()
            else:
                continue
    print(int(pow(2, (n - 1) / 2) % (pow(10, 9) + 7)))
else:
    for i in range(1, n, 2):
        if a_list.count(i) != 2:
            print(0)
            exit()
        else:
            continue
    print(int(pow(2, n / 2) % (pow(10, 9) + 7)))
