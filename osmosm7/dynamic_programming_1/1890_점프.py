#1890_점프.py
n = int(input())
mat = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1
for y in range(n):
    for x in range(n):
        if mat[y][x] !=0:
            if y+mat[y][x] in range(n):
                dp[y+mat[y][x]][x] += dp[y][x]
            if x+mat[y][x] in range(n):
                dp[y][x+mat[y][x]] +=dp[y][x]
print(dp[-1][-1])