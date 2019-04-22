#!/home/shino/.pyenv/shims/python
# https://beta.atcoder.jp/contests/abc105/submissions/2995023
n = int(input())
ans = ""

if n == 0:
    print(0)
    exit()

while n != 0:
    if n % 2 != 0:
        n -= 1
        ans = "1" + ans
    else:
        ans = "0" + ans
    n /= -2
    print(n, ans)#TODO

print(ans)
