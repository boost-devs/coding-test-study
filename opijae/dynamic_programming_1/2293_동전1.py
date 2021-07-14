import sys
input = sys.stdin.readline
n,k=map(int, input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))
dp=[0]*(k+1)
dp[0]=1
for i in arr: # 모든 경우에 대해 돔
    for j in range(i,k+1):
        dp[j]+=dp[j-i] # 동전의 값 간격마다 더해줌
print(dp)
print(dp[k])