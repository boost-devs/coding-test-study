# https://www.acmicpc.net/problem/1260

import sys
from collections import deque
def dfs(start):
    print(start,end=" ")
    visited[start]=True
    for i in range(1,n+1):
        if graph_list[start][i]==1 and not visited[i]:
            dfs(i)

def bfs(start):
    q=deque([start])
    visited[start]=False
    while(q):
        node=q.popleft()
        print(node,end=" ")
        for i in range(1,n+1):
            if graph_list[node][i]==1 and visited[i]:
                q.append(i)
                visited[i]=False

input = sys.stdin.readline
n,m,v=map(int,input().split())
graph_list=[[0 for _ in range(n+1)]for _ in range(n+1)]  # n+1 * n+1 짜리 2차원 배열 -> 연결되어 있는 점은 1 아니면 0
visited=[False for _ in range(n+1)]
for _ in range(m):
    s,e=map(int,input().split())
    graph_list[s][e]=1
    graph_list[e][s]=1
dfs(v)   # visited True가 방문한것
print()
bfs(v)  # visited False가 방문한것
