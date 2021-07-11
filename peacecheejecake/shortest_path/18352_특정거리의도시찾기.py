# https://www.acmicpc.net/problem/18352
# 특정 거리의 도시 찾기
# 105900 KB / 2940 ms


import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())
x -= 1
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = [int(x) - 1 for x in input().split()]
    graph[a].append(b)

dists = [INF] * n
dists[x] = 0
pq = [(0, x)]
while pq:
    dist, city = heapq.heappop(pq)
    if dist > dists[city]:
        continue
    
    for city_ in graph[city]:
        dist_ = dist + 1
        if dist_ < dists[city_]:
            dists[city_] = dist_
            heapq.heappush(pq, (dist_, city_))

cands = [c for c, d in enumerate(dists) if d == k]
if cands:
    for c in sorted(cands):
        print(c + 1)
else:
    print(-1)
