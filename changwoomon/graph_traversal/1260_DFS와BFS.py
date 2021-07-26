###### 1260번: DFS와 BFS
# https://www.acmicpc.net/problem/1260
# 메모리/시간: 32984KB / 104ms

import sys
from collections import deque

input = sys.stdin.readline

# DFS 메서드 정의
def dfs(v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)

# BFS 메서드 정의
def bfs(start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i, x in enumerate(graph):
    x.sort()

dfs_visited = [False for _ in range(N+1)]
bfs_visited = [False for _ in range(N+1)]

dd = dfs(V, dfs_visited)
print()
bb = bfs(V, bfs_visited)