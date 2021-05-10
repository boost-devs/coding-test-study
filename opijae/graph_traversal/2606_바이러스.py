# https://www.acmicpc.net/problem/2606

import sys
from collections import deque
input=sys.stdin.readline

def dfs(start):
    global cnt
    visited[start]=True
    cnt+=1   # 재귀 들어갈 때마다 cnt ++
    for i in range(1,n+1):
        if computer[start][i]==1 and not visited[i]:
            dfs(i)

def bfs(start):
    global cnt
    q=deque([start])
    cnt+=1    # 큐에 넣을때 마다 cnt++
    visited[start]=True
    while q:
        node=q.popleft()
        for i in range(1,n+1):
            if computer[node][i]==1 and not visited[i]:
                q.append(i)
                visited[i]=True
                cnt+=1
n=int(input())
m=int(input())

computer=[[0 for _ in range(n+1)]for _ in range(n+1)]
visited=[False for _ in range(n+1)]
cnt=-1
for _ in range(m):
    s,e=map(int,input().split())
    computer[s][e]=1
    computer[e][s]=1

# dfs(1)
bfs(1)
print(cnt)