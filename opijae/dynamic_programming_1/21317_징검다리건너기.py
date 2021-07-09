import sys
input = sys.stdin.readline

n = int(input())
arr = [[0, 0]]
for _ in range(n-1):
    arr.append(list(map(int, input().split())))
k = int(input())

dp = [[100000, 100000] for _ in range(n+1)]
dp[1][0] = 0
if n > 1:
    dp[2][0] = arr[1][0] # 큰 점프가 불가능할때
if n > 2:
    dp[3][0] = min(dp[2][0] + arr[2][0], arr[1][1]) # 매우 큰점프가 불가능할떄
for i in range(4, n+1):
    dp[i][0] = min(dp[i-1][0] + arr[i-1][0], dp[i-2][0] + arr[i-2][1]) # 매우 큰점프 사용 x
    dp[i][1] = min(dp[i-3][0] + k, dp[i-2][1] + arr[i-2][1], dp[i-1][1] + arr[i-1][0]) # 매우 큰점프 사용

print(min(dp[n]))