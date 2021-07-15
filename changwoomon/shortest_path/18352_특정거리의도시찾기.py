###### 18352번: 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352
# 메모리/시간: 98996KB / 1636ms

import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

_graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    _graph[a].append(b)

visited = [False] * (N+1)

answer = []

def bfs(start):
    queue = deque([(start, 0)])
    visited[start] = True
    while queue:
        for _ in range(len(queue)):
            x, cnt = queue.popleft()
            if cnt == K:
                answer.append(x)
            elif cnt < K:
                for z in _graph[x]:
                    if not visited[z]:
                        visited[z] = True
                        queue.append((z, cnt+1))

bfs(X)

print("\n".join(map(str, sorted(answer)))) if len(answer) >= 1 else print(-1)