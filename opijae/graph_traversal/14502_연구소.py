import sys
from itertools import combinations
from collections import deque
def bfs():
    q=deque(virus)
    cnt=len(q)
    visited=[[False for _ in range(m)]  for _ in range(n)]
    # print(q)
    while q:
        i,j=q.popleft()
        # print(i,j)
        visited[i][j]=True
        for di,dj in directions:
            ni=i+di
            nj=j+dj
            if 0<=ni<n and 0<=nj<m :
                if temp_map[ni][nj]=='0' and not visited[ni][nj]:
                    q.append([ni,nj])
                    cnt+=1
                    visited[ni][nj]=True
                    # temp_map[ni][nj]=2
    return cnt
input = sys.stdin.readline

n,m=map(int,input().split())

_map=[]
virus=[]
safe=[]
for i in range(n):
    temp=[]
    for j,s in enumerate(input().split()):
        temp.append(s)
        if s=='0':
            safe.append([i,j])
        elif s=='2':
            virus.append([i,j])
    _map.append(temp)
print(_map)
directions=[[0,1],[-1,0],[1,0],[0,-1]]
comb_list=combinations(safe,3)
_max=100000
for comb in comb_list:
    temp_map=_map[:]
    # print(_map)
    for i,j in comb:
        temp_map[i][j]=1
    _max=min(_max,bfs())
print(_max)