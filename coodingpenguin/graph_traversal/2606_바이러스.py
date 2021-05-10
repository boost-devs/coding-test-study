# 문제: [BOJ 2606] 바이러스
# 유형: DFS, BFS

import sys

input = sys.stdin.readline


def dfs(v, visited=[]):
    # 현재 노드를 방문 처리
    visited.append(v)
    # 인접 노드 탐색
    for i in graph[v]:
        if i not in visited:
            dfs(i, visited)
    return visited


# 입력
n = int(input())  # 컴퓨터 수
l = int(input())  # 연결 수
links = [list(map(int, input().split())) for _ in range(l)]

# 연결 리스트 생성
graph = [[] for _ in range(n + 1)]
for a, b in links:
    graph[a].append(b)
    graph[b].append(a)

# 깊이 너비 탐색
visited = []
visited = dfs(1, visited)

# 감염된 컴퓨터 수 출력
print(len(visited) - 1)
