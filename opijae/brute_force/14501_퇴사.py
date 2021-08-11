import sys
input = sys.stdin.readline
n= int(input())
arr =[0]*(n+6)
_max =0
for i in range(1,n+1):
    day,pay = map(int, input().split())
    arr[i+day-1] = max(arr[i+day-1], _max+pay)
    _max = max(_max,arr[i]) # 그 전날까지의 최대값을 알아야됨
print(max(arr[:n+1]))