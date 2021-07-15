import sys
input = sys.stdin.readline
n= int(input())
stairs=[0]
for _ in range(n):
    stairs.append(int(input()))
dp=[0,stairs[1]] # dp에는 i번 까지의 계단을 밟았을때 최대 점수를 기록한 배열이다.
if n>1:
    dp.append(stairs[1]+stairs[2])
for i in range(3,n+1):
    # OXO , OXOO 경우를 생각하면된다.(X는 안밟음, O는 밟음)
    # OXO는 그 전 계단을 밟든 안밟든 상관 없기 떄문에 신경안써준다.
    dp.append(max(dp[i-2]+stairs[i],dp[i-3]+stairs[i-1]+stairs[i])) 
print(dp[n])