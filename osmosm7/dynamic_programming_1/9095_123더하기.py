n = int(input())
lst =[]
for i in range(n):
    lst.append(int(input()))
max_num = max(lst)
dp = [1]*(max_num+1)
dp[2] = 2
dp[3] = 4
for i in range(3,max_num+1):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

for i in lst:
    print(dp[i])