#11055_가장큰증가부분수열.py
n = int(input())
lst = list(map(int,input().split()))

dp = lst[:]
for i in range(1,n):
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i],dp[j] + lst[i])
print(max(dp))