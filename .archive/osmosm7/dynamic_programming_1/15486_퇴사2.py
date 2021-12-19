#15486_퇴사2.py
import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * (n+1)
moneys = [0]* (n)
days = [0]* (n)
# 각각에 대해 하거나 안하거나
for i in range(n):
    days[i],moneys[i] = map(int,input().split())
    
for i in range(n):
    if i+days[i] < n+1:
        dp[i+days[i]] = max(dp[i+days[i]],dp[i]+moneys[i])
    dp[i+1] = max(dp[i],dp[i+1])
        
print(dp[-1])