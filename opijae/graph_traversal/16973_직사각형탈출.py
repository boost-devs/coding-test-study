# https://www.acmicpc.net/problem/16973
import sys
from collections import deque
input= sys.stdin.readline
n,m=map(int,input().split())
# 패딩을 1로 줍니다
_map=[['1' for _ in range(m+2)]]
directions=[[0,1],[-1,0],[1,0],[0,-1]]
walls=[]
for i in range(n):
    line=['1']
    for j,s in enumerate(input().split()):
        line.append(s)
        if s=='1':  # 벽인 부분을 찾음
            walls.append((i+1,j+1))
    line.append('1')
    _map.append(line)
_map.append(['1' for _ in range(m+2)])

h,w,s_i,s_j,f_i,f_j=map(int,input().split()) # 높이, 가로? 시작점, 끝점 받음
q=deque([(s_i,s_j,0)])  # 시작점, 이동횟수
visited=[[False]*(m+2) for _ in range(n+2)]
visited[1][1]=True
def bfs():
    while q: 
        i,j,cnt=q.popleft()
        if i==f_i and j==f_j: # 도착점에 도달하면 return
            return cnt
        for di,dj in directions:
            ni=di+i
            nj=dj+j
            if not visited[ni][nj] and 0<ni<n+2-h and 0<nj <m+2-w: # 방문하지 않았고, 좌표가 _map을 벗어나면 안됨
                for w_i,w_j in walls:
                    if ni<=w_i<=ni+h-1 and nj<=w_j<=nj+w-1:
                        break
                else:
                    visited[ni][nj]=True
                    q.append((ni,nj,cnt+1))
    return -1
print(bfs())