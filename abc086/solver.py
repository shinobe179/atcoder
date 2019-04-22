#!/home/shino/.anyenv/envs/pyenv/shims/python

ab = int(input().replace(" ",""))

for i in range(0, 101):
    if ab == i ** 2:
        print("Yes")
        exit()
    if i ** 2 > 100100:
        break

print("No")
