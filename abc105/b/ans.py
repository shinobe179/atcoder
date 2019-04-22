#!/home/shino/.pyenv/shims/python 
n = int(input())

if n < 4:
    print('No')
    exit()
elif n % 7 == 0 or n % 4 == 0:
    print('Yes')
    exit()
elif n % 7 % 4 == 0 or n % 4 % 7 == 0:
    print('Yes')
    exit()
else:
    for i in range(1, n % 7):
        tmp = n - 7 * i
        if tmp < 0:
            break
        elif tmp % 4 == 0:
            print('Yes')
            exit()
    for i in range(1, n & 4):
        tmp = n - 4 * i
        if tmp < 0:
            break
        elif tmp % 7 == 0:
            print('Yes')
            exit()

print('No')
