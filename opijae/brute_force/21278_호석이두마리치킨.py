import sys
from itertools import combinations
input = sys.stdin.readline
n,m = map(int, input().split())
arr = [ [10000000]*(n) for _ in range(n)]  # 최대값으로 초기화

for _ in range(m):
    a,b = map(int, input().split())
    a -=1
    b -=1
    # 거리 정보
    arr[a][b] = 1
    arr[b][a] = 1 
# 플로이드 마셜로 모든 노드 간에 거리 구하기
for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][j]>arr[i][k]+arr[k][j]:
                arr[i][j]=arr[i][k]+arr[k][j]
            if i ==j:
                arr[i][j] = 0
_min = 1000000  # 최소 값
_p1,_p2=10000,1000000 # 최소값을떄 좌표
min_list = []
combs = combinations(range(n),2)
for i,j in combs:
    _sum = 0
    for house in range(n): # 모든 집마다
        if house == i or house == j: # 같으면 치킨집이 지어졌으니 거리==0
            continue
        _temp = 2*min(arr[house][i],arr[house][j]) # 두 치킨집중 가까운 거리
        _sum += _temp
    if _min>_sum:
        _min = _sum
        _p1,_p2 = i,j # i,j가 작은거 부터 도니 따로 확인 안해줘도 된ㄴ다.
print(_p1+1,_p2+1,_min)
