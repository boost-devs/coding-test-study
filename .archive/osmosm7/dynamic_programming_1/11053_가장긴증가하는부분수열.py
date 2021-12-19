#11053_가장긴증가하는부분수열.py
n = int(input())
lst = list(map(int,input().split()))
dp = [0] * n
dp[0] = 1
for i in range(1,n):
    max_len = 1
    now = lst[i]
    for j in range(i):
        if lst[j] < now:
            max_len = max(max_len,dp[j] +1)
    dp[i] = max_len
print(max(dp))