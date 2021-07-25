import sys
input = sys.stdin.readline
n= int(input())
# dates = [0] * 366
# for _ in range(n):
#     s,e = map(int, input().split())
#     for i in range(s,e+1):
#         dates[i] +=1

# _height = 0
# _width = 0
# ans = 0
# for date in dates:
#     if date !=0 :
#         _width +=1
#         _height = max(_height, date)
#     else:
#         ans += _height * _width
#         _height = 0
#         _width = 0
# ans += _height * _width
# print(ans)
Q = [0] * 367 # 증감 배열
D = [0] # 특정 날 일정 수

for _ in range(n):
    p, q = map(int, input().split())
    Q[p] += 1 # 시작날 ++
    Q[q + 1] -= 1 # 끝나는 날  --

_height = 0
_width = 0
ans = 0
for i in range(1,366):
    D.append(Q[i] + D[i-1]) # 그날의 일정은 그 전날 일정 + 현재 날의 증감 배열
    if D[i] ==0:
        ans += _height*_width
        _height = 0
        _width = 0
    else:
        _width += 1
        _height = max(D[i],_height)
ans += _height*_width
print(ans)