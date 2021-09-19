# 문제: [BOJ 11725] 트리의 부모 찾기
# 유형: BFS
# 메모리/시간: 57556kb / 412ms

import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def bfs(start):
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                parent[i] = v  # 부모테이블 갱신
                visited[i] = True
                queue.append(i)


# 입력
n = int(input())  # 노드 수
graph = defaultdict(list)  # 연결 리스트
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = list(range(n + 1))  # 부모테이블
visited = [False] * (n + 1)  # 방문여부

# 너비 우선 탐색
bfs(1)

# 출력
for i in parent[2:]:
    print(i)
