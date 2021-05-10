# 문제: [BOJ 1260] DFS와 BFS
# 유형: DFS, BFS

import sys
from collections import deque

input = sys.stdin.readline


def dfs(v, visited=[]):
    # 현재 노드를 방문 처리
    visited.append(v)
    # 인접 노드 탐색
    for i in graph[v]:
        if i not in visited:
            visited = dfs(i, visited)
    return visited


def bfs(start, visited=[]):
    visited.append(start)  # 시작 노드 방문 처리
    queue = deque([start])  # 인접한 노드를 저장하는 큐 생성
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
    return visited


# 입력
n, m, v = map(int, input().split())
links = [list(map(int, input().split())) for _ in range(m)]

# 인접 리스트 생성
graph = [[] for _ in range(n + 1)]
for a, b in links:
    graph[a].append(b)
    graph[b].append(a)

# 인접 리스트 그래프 정렬
for nodes in graph:
    nodes.sort()

# 그래프 탐색
dfs_visited = dfs(v)
bfs_visited = bfs(v)

# 출력
print(" ".join(map(str, dfs_visited)))
print(" ".join(map(str, bfs_visited)))
