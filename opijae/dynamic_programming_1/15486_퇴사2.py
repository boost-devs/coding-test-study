import sys
input = sys.stdin.readline
def solve():
    n= int(input())
    arr=[0]*(n+1)
    _max=0
    for i in range(n):
        t,p=map(int, input().split())
        _max=max(_max,arr[i])
        if t+i>n:
            continue
        if arr[i+t]<p+_max:
            arr[i+t]=p+_max
#     arr[i+t]=max(arr[i+t],_max+p)
    _max=max(_max,arr[i+1])
    print(_max)
    # print(max(arr))

solve()