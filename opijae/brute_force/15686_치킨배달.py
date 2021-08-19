import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int, input().split())
arr = []  # 맵 배열
chicken = [] # 치킨 위치
houses = [] # 집 위치
for i in range(n):
    _input = list(map(int, input().split()))
    arr.append(_input)
    for j in range(n):
        if _input[j] == 2:
            chicken.append((i,j))
        elif _input[j] == 1:
            houses.append((i,j))
combs = combinations(chicken,len(chicken) - m)
_min = 10000000000
for comb in combs: # 치킨집 없애는 조합
    _chickens = [] # 살아 있는 치킨집
    for i,j in chicken:
        if (i,j) not in comb:
            _chickens.append((i,j))
    _temp = 0 # local min
    for h_i,h_j in houses: # 모든 집이랑 살아있는 치킨 위치 돌기
        __min = 100000000
        for c_i,c_j in _chickens:
            __min = min(__min,(abs(h_i - c_i) + abs(h_j - c_j)))
        _temp += __min
    _min = min(_min,_temp)
print(_min)
