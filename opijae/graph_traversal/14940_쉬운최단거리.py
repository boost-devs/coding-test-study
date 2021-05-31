# https://www.acmicpc.net/problem/14940
import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int,input().split())
directions=[[0,1],[-1,0],[1,0],[0,-1]]
_map=[]
for i in range(n):
    line=[]
    for j,s in enumerate(input().split()):
        if s=='2': # 시작점 찾기
            si,sj=i,j
        line.append(int(s))
    _map.append(line)

q=deque([(si,sj)])
while q:
    i, j = q.popleft()
    for di,dj in directions:
        ni, nj = i+di, j+dj
        if 0 <= ni < n and 0 <= nj < m and _map[ni][nj] == 1: # 범위 안에 있고 _map값이 1이면
            q.append((ni, nj))
            _map[ni][nj] = _map[i][j]+1 # 그 전 값에 ++

for i in range(n):
    for j in range(m):
        dist = _map[i][j]
        if dist==0:
            print(dist,end=' ')
        else:
            print(dist-2,end=' ') # 시작점이 2 부터 시작하니 여기서 2를 빼줌
    print()

