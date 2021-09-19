# 문제: [BOJ 1753] 최단경로
# 유형: 다익스트라
# 메모리/시간: 67660kb / 772ms

import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, current = heapq.heappop(queue)
        # 처리된 노드라면 패스
        if distance[current] < dist:
            continue
        # 연결된 노드에 대해서
        for e, w in graph[current]:
            new_dist = dist + w  # 새로운 비용
            # 기존보다 작다면
            if new_dist < distance[e]:
                distance[e] = new_dist  # 최단거리 테이블 갱신
                heapq.heappush(queue, (new_dist, e))  # 우선순위 큐에 추가


v, e = map(int, input().split())  # 노드 수, 간선 수
k = int(input())  # 시작 노드
graph = defaultdict(list)  # 연결 리스트
for _ in range(e):
    s, e, w = map(int, input().split())
    # s에서 e로 가는 데 비용은 w
    graph[s].append((e, w))
distance = [INF] * (v + 1)  # 최단거리 테이블

# 다익스트라 수행
dijkstra(k)
for i in range(1, v + 1):
    # 경로가 존재하지 않는 경우
    if distance[i] == INF:
        print("INF")
    # 경로가 존재하는 경우
    else:
        print(distance[i])
