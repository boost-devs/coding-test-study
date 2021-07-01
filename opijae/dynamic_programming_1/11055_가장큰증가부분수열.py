import sys
input = sys.stdin.readline
n= int(input())
arr=list(map(int, input().split()))
dp=arr[:]
for i in range(n):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i]=max(dp[i],dp[j]+arr[i]) # i번째 기준 최대값 구하기
print(max(dp))