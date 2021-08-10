import sys
from itertools import combinations
input = sys.stdin.readline
n,m = map(int, input().split())
combs = combinations(range(m),3) # 선택할 수 있는 열 조합
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

_max = 0
for a,b,c in combs:
    _sum = 0
    for ar in arr:
        _sum+= max(ar[a],ar[b],ar[c]) # 현재 선택된 열중 최대값
    _max = max(_max,_sum)
print(_max)