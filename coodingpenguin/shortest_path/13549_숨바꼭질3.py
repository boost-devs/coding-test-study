# 문제: [BOJ 13549] 숨바꼭질 3
# 유형: 다익스트라
# 메모리/시간: 70572kb / 1708ms

import sys
import heapq

input = sys.stdin.readline
INF, MAX = int(1e9), int(1e6)


def dijkstra(start, end):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, current = heapq.heappop(queue)
        # 이미 처리한 노드면 패스
        if distance[current] < dist:
            continue
        # 도착지점이라면 반환
        if current == end:
            return distance[end]
        next_pos = [(current - 1, 1), (current + 1, 1), (current * 2, 0)]  # 갈 수 있는 위치
        for v, w in next_pos:
            # 범위 내이고
            if 0 <= v <= MAX:
                new_dist = dist + w  # 새로운 비용
                # 기존보다 작다면
                if new_dist < distance[v]:
                    distance[v] = new_dist  # 갱신
                    heapq.heappush(queue, (new_dist, v))  # 우선순위 큐에 추가


n, k = map(int, input().split())  # 수빈 위치, 동생 위치
distance = [INF] * (MAX + 1)  # 최단 거리 테이블

# 다익스트라 수행
print(dijkstra(n, k))
