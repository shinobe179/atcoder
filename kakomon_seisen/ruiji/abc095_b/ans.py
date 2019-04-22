#!/home/shino/.pyenv/shims/python
n, x = map(int, input().split())
list_m = [int(input()) for i in range(n)]
ans = len(list_m)
x -= sum(list_m)
print(str(ans + x // min(list_m)))
