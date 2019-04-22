n, a, b = map(int, input().split())
ans = 0


def sum_digit(i):
    s = str(i)
    l = list(map(int, list(s)))
    return sum(l)


for i in range(n + 1):
    if a <= sum_digit(i) and b >= sum_digit(i):
        ans += i

print(ans)
