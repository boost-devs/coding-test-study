# https://www.acmicpc.net/problem/13549
# 숨바꼭질 3
#


import heapq

INF = int(1e6) + 1

n, k = map(int, input().split())
num_verts = int(2 * 1e5) + 1
graph = [[] for _ in range(num_verts)]
for x in range(num_verts):
    edges = []
    if x > 0:
        edges.append((x - 1, 1))
    if x < num_verts - 1:
        edges.append((x + 1, 1))
    if 2 * x < num_verts:
        edges.append((2 * x, 0))
    graph[x].extend(edges)

times = [INF] * num_verts
times[n] = 0
pq = [(0, n)]
while pq:
    t, x = heapq.heappop(pq)
    if times[x] >= t:
        for nx, dt in graph[x]:
            nt = t + dt
            if times[nx] > nt:
                times[nx] = nt
                heapq.heappush(pq, (nt, nx))

print(times[k])
