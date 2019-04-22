#!/home/shino/.anyenv/envs/pyenv/shims/python

n = int(input())
h_list = [int(_) for _ in input().split()]
ans = 0
while sum(h_list) != 0:
    # 0で区切られた、1以上の数のかたまりを数える
    # 要素が全て1以上ならansに+1して次のループ
    if h_list.count(0) == 0:
        ans += 1
    else:
        for i in range(1, n):
            # 1以上から0に下がった時にかたまりをカウント
            if h_list[i] == 0 and h_list[i - 1] != 0:
                ans += 1
            elif i == n - 1 and h_list[i] != 0:
                ans += 1
    # 1以上の箇所を1段ずつ落とす
    for i in range(n):
        if h_list[i] != 0:
            h_list[i] -= 1

print(ans)
