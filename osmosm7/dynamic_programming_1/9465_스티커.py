#9465_스티커.py

n = int(input())

for _ in range(n):
    m = int(input())
    post = [list(map(int,input().split())) for k in range(2)]
    
    dp = [[0] * m for z in range(2)]
    dp[0][0] = post[0][0]
    dp[1][0] = post[1][0]
    
    dp[0][1] = post[0][1] + post[1][0]
    dp[1][1] = post[0][0] + post[1][1]
    
    for i in range(2,m):
        for b in range(2):
            dp[b][i] = max(post[b][i]+max(dp[0][i-2],dp[1][i-2]),dp[1-b][i-1]+post[b][i])
    print(max(dp[0][-1],dp[1][-1]))