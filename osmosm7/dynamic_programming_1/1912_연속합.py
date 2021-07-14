#1912_연속합.py
n = int(input())
lst = list(map(int,input().split()))
dp = [0] * n
dp[0] = lst[0]

for i in range(1,n):
    if dp[i-1] < 0:
        dp[i] = lst[i]
    else:
        dp[i] = dp[i-1] + lst[i]
print(max(dp))