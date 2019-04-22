n = int(input())
a_list = list(map(int, input().split()))
alice = 0
bob = 0


for i in range(len(a_list)):
    if i % 2:
        bob += sorted(a_list, reverse=True)[i]
    else:
        alice += sorted(a_list, reverse=True)[i]

#print(str(alice - bob))
print(str(alice - bob), str(alice), str(bob))
