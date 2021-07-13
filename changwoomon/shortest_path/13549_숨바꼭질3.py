###### 13549번: 숨바꼭질 3
# https://www.acmicpc.net/problem/13549
# 메모리/시간: 35124KB / 256ms

import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

N, K = map(int, input().split())

distance = [INF] * 100001

f1 = lambda x: x-1
f2 = lambda x: x+1
f3 = lambda x: 2*x
func = [f3, f1, f2]

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, x = heapq.heappop(queue)
        if x == K:
            return dist
        if distance[x] < dist:
            continue
        for i in range(3):
            z = func[i](x)
            if (z < 0) or (z > 100000) or (distance[z] != INF):
                continue
            if i == 0:
                distance[z] = min(distance[z], dist)
            else:
                distance[z] = min(distance[z], dist+1)
            heapq.heappush(queue, (distance[z], z))

print(dijkstra(N))