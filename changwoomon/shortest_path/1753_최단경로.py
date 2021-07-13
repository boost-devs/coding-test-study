###### 1753번: 최단경로
# https://www.acmicpc.net/problem/1753
# 메모리/시간: 66044KB / 748ms

import sys
import heapq

input = sys.stdin.readline

INF = int(1e6)

V, E = map(int, input().split())

graph = [[] for i in range(V + 1)]
distance = [INF] * (V + 1)

K = int(input())

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start=K):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, x = heapq.heappop(queue)
        if distance[x] < dist:
            continue
        for z in graph[x]:
            cost = dist + z[1]
            if cost < distance[z[0]]:
                distance[z[0]] = cost
                heapq.heappush(queue, (cost, z[0]))

dijkstra(K)

for x in distance[1:]:
    print(x if x != INF else "INF")