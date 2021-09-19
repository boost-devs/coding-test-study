# 문제: [BOJ 11725] 트리의 부모 찾기
# 유형: BFS
# 메모리/시간: 56808kb / 404ms

import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def bfs(start):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            # 부모 테이블이 갱신되지 않았다면
            if parent[i] == i:
                parent[i] = v  # 갱신
                queue.append(i)  # 큐에 삽입


# 입력
N = int(input())  # 노드 수
graph = defaultdict(list)  # 간선 정보
for _ in range(N - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

parent = [i for i in range(N + 1)]  # 부모 테이블

# 너비 우선 탐색
bfs(1)

# 출력
for p in parent[2:]:
    print(p)
