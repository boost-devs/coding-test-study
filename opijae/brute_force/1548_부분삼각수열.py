import sys
from itertools import combinations
input = sys.stdin.readline
n= int(input().strip())

arr = list(map(int, input().split()))
combs = combinations(range(n),3)
_max = 2
if n <3:
    print(n)
    exit()
arr.sort()
for i,j,k in combs:
    if arr[i]+arr[j]>arr[k]:
        _max = max(k-j+2,_max)
print(_max)