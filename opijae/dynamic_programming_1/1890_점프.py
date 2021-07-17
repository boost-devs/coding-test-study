import sys
input = sys.stdin.readline
n= int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int, input().split())))
dp = [[0]*n for _ in range(n)] # dp 배열 생성
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if arr[i][j]==0: # 0이면 넘어가기
            continue
        if i+arr[i][j] < n: # 오른쪽으로 점프가 가능한지
            dp[i+arr[i][j]][j] += dp[i][j]
        if j+arr[i][j] <n: # 왼쪽으로 점프가 가능한지
            dp[i][j+arr[i][j]] += dp[i][j]

print(dp[n-1][n-1])