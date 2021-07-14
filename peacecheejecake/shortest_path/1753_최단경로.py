# https://www.acmicpc.net/problem/1753
# 최단경로
# 66044 KB / 736 ms


import heapq
import sys

input = sys.stdin.readline

INF = int(1e7)

num_verts, num_edges = map(int, input().split())
start = int(input()) - 1
graph = [[] for _ in range(num_verts)]
for _ in range(num_edges):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w))

distances = [INF] * num_verts
distances[start] = 0

pq = [(0, start)]
while pq:
    dist, v = heapq.heappop(pq)
    if distances[v] >= dist:
        for a, w in graph[v]:
            dist_to_adj = dist + w
            if distances[a] > dist_to_adj:
                distances[a] = dist_to_adj
                heapq.heappush(pq, (dist_to_adj, a))

for distance in distances:
    if distance < INF:
        print(distance)
    else:
        print('INF')
