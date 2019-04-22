#!/home/shino/.pyenv/shims/python
#import math
#
#n = int(input())
#p_list = [list(map(int, input().split())) for i in range(n)]
#ans = 0
#
#for a in p_list:
#    for b in p_list:
#        if a == b:
#            continue
#        else:
#            c = [a[0], b[1]]
#            tmp_ans = math.sqrt((a[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2)
#            print(a, b, c, tmp_ans)
#            if ans < tmp_ans:
#                ans = tmp_ans
#
#print(ans)
N=int(input())
S = []

for i in range(0,N):
    XY=input().split(" ")
    S.append((int(XY[0]),int(XY[1])))
print(S)
ma=0.0
for i in range(0,N):
    for j in range(0,N):
        ma=max(ma, ((S[i][0]-S[j][0])**2+(S[i][1]-S[j][1])**2)**0.5)

print(ma)
