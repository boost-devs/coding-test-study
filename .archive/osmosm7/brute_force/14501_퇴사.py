n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
dp = [0] * (n+1)
for i in range(n):
    dp[i] = max(dp[i],dp[i-1])
    day, money = lst[i]
    if i + day in range(n+1):
        dp[i+day] = max(dp[i+day],dp[i]+money)
print(max(dp))