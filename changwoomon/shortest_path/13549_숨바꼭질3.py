###### 13549번: 숨바꼭질 3
# https://www.acmicpc.net/problem/13549
# 메모리/시간: 35124KB / 256ms

import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

N, K = map(int, input().split())

time_table = [INF] * 100001

f1 = lambda x: x-1
f2 = lambda x: x+1
f3 = lambda x: 2*x
func = [f3, f1, f2]

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    time_table[start] = 0
    while queue:
        time, x = heapq.heappop(queue)
        if x == K:
            return time
        if time_table[x] < time:
            continue
        for i in range(3):
            z = func[i](x)
            if (z < 0) or (z > 100000) or (time_table[z] != INF):
                continue
            if i == 0:
                time_table[z] = min(time_table[z], time)
            else:
                time_table[z] = min(time_table[z], time+1)
            heapq.heappush(queue, (time_table[z], z))

print(dijkstra(N))