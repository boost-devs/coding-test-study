#108444_쉬운계단수.py
n = int(input())
dp = [[0] * (n) for i in range(10)]
for i in range(len(dp)):
    dp[i][0] = 1
for i in range(1,len(dp[0])):
    for j in range(len(dp)):
        if j ==0:
            dp[j][i] = dp[j+1][i-1]
        elif j == 9:
            dp[j][i] = dp[j-1][i-1]
        else:
            dp[j][i] = dp[j-1][i-1] + dp[j+1][i-1]
lst = []
for j in range(len(dp[0])):
    s = 0
    for i in range(1,len(dp)):
        s += dp[i][j]
    lst.append(s)
print(lst[n-1]%1000000000)