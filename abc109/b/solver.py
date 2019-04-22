#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys

n = int(input())
w_list = [input() for _ in range(n)]
for i in range(1, len(w_list)):
    if w_list[i - 1][-1] == w_list[i][0]:
        if not w_list[i] in w_list[0:i]:
            pass
        else:
            print("No")
            sys.exit(0)
    else:
        print("No")
        sys.exit(0)

print("Yes")
