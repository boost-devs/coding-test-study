#2579_계단오르기.py
import sys
input = sys.stdin.readline
n = int(input())
steps= [0]
for _ in range(n):
    steps.append(int(input()))

dp = [0] * (n+1)
if n ==1:
    print(steps[1])
    sys.exit()
if n ==2:
    print(steps[1]+steps[2])
    sys.exit()
    
dp[1] = steps[1]
dp[2] = steps[1] + steps[2]

for i in range(3,n+1):
    dp[i] = max(dp[i-2],dp[i-3]+steps[i-1]) + steps[i]
print(dp[n])