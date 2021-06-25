import sys
input = sys.stdin.readline
n= input().rstrip()
# 놓을 수 있는 경우가 1,3이기 때문에 n이 홀수 라면 SK가 이긴다.
# 1,3,5,7 .....
if int(n[-1])%2==0:
    print('CY')
else:
    print('SK')
