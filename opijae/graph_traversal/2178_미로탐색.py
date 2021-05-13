# https://www.acmicpc.net/problem/2178

import sys
from collections import deque

def bfs():
    q=deque([[1,1]])
    while q:
        node=q.popleft()
        for i in range(4):
            nx=node[0]+dx[i]
            ny=node[1]+dy[i]
            if maze[nx][ny]==1:
                q.append([nx,ny])
                maze[nx][ny]=maze[node[0]][node[1]]+1 # dp 처럼 게속 가중치를 더해줌 
input=sys.stdin.readline

n,m = map(int,input().split())
# 4방향 탐색
dx=[-1,0,1,0]
dy=[0,-1,0,1]
maze=[[0 for _ in range(m+2)]]
for _ in range(n):
    line=list(map(int,list(input().rstrip())))
    line.insert(0,0)
    line.append(0)
    maze.append(line)
maze.append([0 for _ in range(m+2)])
# maze는 n+2*n+2짜리 배열 외각을 0으로 padding
bfs()
print(maze[n][m])
