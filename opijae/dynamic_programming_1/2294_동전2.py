import sys
input = sys.stdin.readline

n,k=map(int, input().split())

arr=set()
for _ in range(n):
    arr.add(int(input()))
dp=[10000000000]*(k+1)
dp[0]=0
for j in arr: # 모든 동전에 대해
    for i in range(j,k+1): # 동전의 값 부터 시작함
        dp[i]=min(dp[i],dp[i-j]+1) # 이전 값에 +1
if dp[k]==10000000000:
    print(-1)
else:
    print(dp[k])