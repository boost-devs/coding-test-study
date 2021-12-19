#2156_포도주시식.py
import sys
input = sys.stdin.readline
n = int(input())
lst = [int(input()) for i in range(n)]
lst.insert(0,0)
if n ==1:
    print(lst[1])
    sys.exit()
if n ==2:
    print(lst[1]+lst[2])
    sys.exit()

dp = [0] * (n+1)
dp[1] = lst[1]
dp[2] = lst[1] + lst[2]
for i in range(3,n+1):
    dp[i] = max(max(dp[:i-1]) ,max(dp[:i-2])+ lst[i-1],)+ lst[i]
print(max(dp))