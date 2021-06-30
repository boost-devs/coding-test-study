import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp=[1] * n
for i in range(n):
    for j in range(i):
        # 현재갑 arr[i]보다 작은 것들 check
        if arr[i]>arr[j]:
            dp[i]=max(dp[i],dp[j]+1) # 길이 갱신
print(max(dp))