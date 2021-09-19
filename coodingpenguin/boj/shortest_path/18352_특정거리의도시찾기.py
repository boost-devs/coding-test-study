# 문제: [BOJ 18352] 특정 거리의 도시 찾기
# 유형: 그래프 탐색
# 메모리/시간: 115656kb / 2492s

import sys
from collections import defaultdict, deque


input = sys.stdin.readline
INF = int(1e9)


def bfs(start):
    queue = deque([start])
    distance[start] = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            # 갱신되지 않았다면
            if distance[i] == INF:
                distance[i] = distance[v] + 1
                queue.append(i)


n, m, k, x = map(int, input().split())  # 도시 개수, 도로 개수, 거리 정보, 출발 도시
distance = [INF] * (n + 1)  # 최단 거리 테이블
graph = defaultdict(list)  # 연결 정보
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 너비 우선 탐색
bfs(x)

# 최단 거리가 k인 도시
result = sorted([i for i, cost in enumerate(distance) if cost == k])
# 있다면
if result:
    for i in result:
        print(i)
# 없다면
else:
    print(-1)
