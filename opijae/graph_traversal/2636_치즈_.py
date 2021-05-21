# https://www.acmicpc.net/problem/2636
#
import sys
from collections import deque
import time as tt
def bfs():
    q=deque([[0,0]])
    visited[0][0]=True
    cnt=0
    while q:
        i,j=q.popleft()

        for di,dj in directions:
            ni=i+di
            nj=j+dj
            if 0<=ni<n and 0<=nj <m:
                if not visited[ni][nj]:
                    visited[ni][nj]=True
                    if _map[ni][nj]=='0':
                        q.append([ni,nj])
                    else:
                        _map[ni][nj]='0'
                        cnt+=1
    return cnt
input=sys.stdin.readline

n,m=map(int,input().split())
directions=[[0,1],[-1,0],[1,0],[0,-1]]
_map=[]
cheese=[]
for i in range(n):
    temp=[]
    for j,s in enumerate(input().split()):
        temp.append(s)
    _map.append(temp)
time=0
while True:
    time+=1
    visited=[[False]*m for _ in range(n)]
    cnt=bfs()  # 녹은 치즈이 개수를 return
    cheese.append(cnt)
    if cnt==0: # 녹은 치즈가 없다면 치즈가 없다는 것이니 종료
        break
print(time-1)
print(cheese[-2]) # 녹기 한시간전 치즈니 뒤에서 두번째