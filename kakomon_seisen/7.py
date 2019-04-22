n = int(input())
list_d = [int(input()) for i in range(n)]
j = 101
ans = 0

for i in sorted(list_d, reverse=True):
    if j <= i:
        continue
    else:
        ans += 1
        j = i

print(ans)
