#2294_동전2.py
n,k = map(int,input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
inf = 10**10
dp = [inf] * (k+1)
dp[0] = 0
for coin in coins:
    for i in range(coin,k+1):
        dp[i] = min(dp[i - coin] + 1 , dp[i])
if dp[-1] == inf:
    print(-1)
else:
    print(dp[-1])