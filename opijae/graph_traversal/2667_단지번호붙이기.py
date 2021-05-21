# https://www.acmicpc.net/problem/2667
import sys
from collections import deque

input=sys.stdin.readline

n=int(input())

_map=[[0 for _ in range(n+2)]]
# 방향 정의
dx=[-1,0,1,0]
dy=[0,-1,0,1]
for _ in range(n):
    line=list(map(int,list(input().rstrip())))
    line.insert(0,0)
    line.append(0)
    _map.append(line)
_map.append([0 for _ in range(n+2)])

# _map은 n+2*n+2짜리 배열 외각을 0으로 padding

ans=[]
for i in range(1,n+1): # 1,1부터 n,n까지 돌기
    for j in range(1,n+1):
        if _map[i][j]==1:
            cnt=1
            q=deque([[i,j]])
            _map[i][j]=0  # 방문한 곳을 0
            while q:
                node=q.popleft()
                for k in range(4): #4방향 탐색
                    nx=node[0]+dx[k]
                    ny=node[1]+dy[k]
                    if _map[nx][ny]==1:
                        q.append([nx,ny])
                        _map[nx][ny]=0 # 방문한 곳을 0
                        cnt+=1
            ans.append(cnt)
print(len(ans))
for i in sorted(ans):
    print(i)