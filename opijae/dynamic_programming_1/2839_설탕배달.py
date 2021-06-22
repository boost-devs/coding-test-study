import sys
input = sys.stdin.readline
n= int(input())
bags=[3,5]
arr=[-1]*(n+1)
arr[0]=0
for bag in bags:
    for i in range(n+1-bag):
        if arr[i]>-1:
            arr[i+bag]=arr[i]+1
print(arr[-1])