#11660_구간합구하기5
n,m = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(n)]
lst = [list(map(int,input().split())) for _ in range(m)]

dp = [[0]*(n) for _ in range(n)]
dp[0][0] = mat[0][0]

for y in range(1,n):
    dp[0][y] = mat[0][y] + dp[0][y-1]
for x in range(1,n):
    dp[x][0] = mat[x][0] + dp[x-1][0]
    
for x in range(1,n):
    for y in range(1,n):
         dp[x][y] = dp[x-1][y] + dp[x][y-1] - dp[x-1][y-1] +mat[x][y]

for x1,y1,x2,y2 in lst:
    x1 -=1
    y1 -=1
    x2 -=1
    y2 -=1
    if x1 >0 and y1>0:
        print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])
    elif x1>0:
        print(dp[x2][y2] - dp[x1-1][y2])
    elif y1>0:
        print(dp[x2][y2] - dp[x2][y1-1])
    else:
        print(dp[x2][y2])