#11727_2xn타일링2.py
n = int(input())
dp = [0] * (n+2)
dp[1] = 1
dp[2] = 3
if n<3:
    print(dp[n])
for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]*2
print(dp[-1]%1007)