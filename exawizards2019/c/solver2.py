#!/home/shino/.anyenv/envs/pyenv/shims/python
import sys
from collections import Counter

# N: マスの数
# Q: 呪文の回数
N, Q = map(int, input().split())
s = input()
s_list = []

for i in range(len(s)):
    s_list.append({'moji':s[i], 'goremu':1})

Q_list = []
for i in range(Q):
    t, d = input().split()


ans = 0
    for i in range(len(s_list)):
        if s_list[i]['moji'] == t:
            if s_list[i]['goremu'] != 0:
                if d == 'L':
                    if i - 1 < 0:
                        s_list[i]['goremu'] = 0
                    else:
                        s_list[i - 1]['goremu'] += s_list[i]['goremu']
                        s_list[i]['goremu'] = 0
                elif d == 'R':
                    if i + 1 >= len(s_list):
                       s_list[i]['goremu'] = 0
                    else:
                       s_list[i + 1]['goremu'] += s_list[i]['goremu']
                       s_list[i]['goremu'] = 0

    #print(t, d)
    #print(s_list)

for i in s_list:
    ans += i['goremu']

#print(ans, s_list)
print(ans)
