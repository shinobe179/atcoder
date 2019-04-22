n = input()
list = [int(i) for i in n]
N = int(n)
m = 0

for i in list:
    m += i

if N % m == 0:
    print("Yes")
else:
    print('No')