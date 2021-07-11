#1106_호텔.py
c,n = map(int,input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int,input().split())))
dp = [10**10] * (1100)
dp[0] = 0
for i in range(n):
    cost, cust = lst[i]
    for j in range(cust,1100):
        dp[j] = min(dp[j-cust] + cost,dp[j])
print(min(dp[c:]))