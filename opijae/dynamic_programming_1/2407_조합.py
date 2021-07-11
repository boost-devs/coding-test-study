import sys
input = sys.stdin.readline
n,m=map(int, input().split())
ans=1
div=1
for i in range(n,n-m,-1):
    ans*=i # n, n-1 .....
    ans//=div # 1,2,3 ....
    div+=1
print(ans)