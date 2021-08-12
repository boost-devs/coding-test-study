import sys
from itertools import combinations,product
input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
_min = 1000000
prods = combinations(product(range(1,n-1),range(1,n-1)),3) # 3점의 죄표 조합 (((0,0),(0,1),(0,2)), ..... )

for (i1,j1),(i2,j2),(i3,j3) in prods:
    # 각 좌표 마다 꽃이 심어질 위치
    flower_map = [(i1-1,j1),(i1,j1),(i1,j1+1),(i1,j1-1),(i1+1,j1),
                    (i2-1,j2),(i2,j2),(i2,j2+1),(i2,j2-1),(i2+1,j2),
                    (i3-1,j3),(i3,j3),(i3,j3+1),(i3,j3-1),(i3+1,j3)]
    # 중복이 없다면 꽃을 심을 수 있다.
    if len(set(flower_map)) == 15:
        _sum = 0
        for i,j in flower_map:
            _sum += arr[i][j]
        _min = min(_min, _sum)
print(_min)
