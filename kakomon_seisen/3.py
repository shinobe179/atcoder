n = input()
il = list(map(int, input().split()))
ans = 0
fin = 0

while fin < 1:
    cnt = 0
    for i in range(len(il)):
        if il[i] % 2:
            fin = 1
            break
        else:
            cnt += 1

    if cnt == len(il):
        for i in range(len(il)):
            il[i] = il[i] / 2
        ans += 1
    else:
        break

print(ans)
