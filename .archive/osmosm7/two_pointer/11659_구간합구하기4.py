import sys

input = sys.stdin.readline
n,m = map(int,input().split())
lst = list(map(int,input().split()))
dp = [0] * (n+1)
for i in range(1,n+1):
    dp[i] = dp[i-1]+lst[i-1]

for _ in range(m):
    a,b = map(int,input().split())
    print(dp[b] - dp[a-1])
