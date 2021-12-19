#1463_1로 만들기.py
import sys
n = int(input())
if n ==1:
    print(0)
    sys.exit()
if n <4:
    print(1)
    sys.exit()
dp = [10**10] * (n+1)
dp[0] = 10**10
dp[1] = 0
dp[2] = 1
dp[3] = 1
for i in range(4,n+1):
    a,b = 0,0
    if i %2 ==0:
        a = int(i//2)
    if i %3 ==0:
        b = int(i//3)
    dp[i] = min(dp[i-1],dp[a],dp[b]) + 1
print(dp[-1])