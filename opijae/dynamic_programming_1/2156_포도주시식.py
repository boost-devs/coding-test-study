import sys
input = sys.stdin.readline
n= int(input())
wine=[0]
for _ in range(n):
    wine.append(int(input()))
dp=[0,wine[1]] # dp에는 i번 까지의 포도주를 마셨을때 최대 양를 기록한 배열이다.
if n>1:
    dp.append(wine[1]+wine[2])
for i in range(3,n+1):
    # OXO , OXOO, OOX 경우를 생각하면된다.(X는 안마심, O는 마심)
    dp.append(max(dp[i-2]+wine[i],dp[i-3]+wine[i-1]+wine[i],dp[i-1]))
print(dp[n])