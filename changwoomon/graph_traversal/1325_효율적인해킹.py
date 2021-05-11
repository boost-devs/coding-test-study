# 1325번: 효율적인 해킹
# https://www.acmicpc.net/problem/1325
# Python3 시간 초과
# PyPy3 시간: 12040 ~ 14836ms

import sys
from collections import deque

input = sys.stdin.readline

# BFS 메서드 정의
def bfs(start, visited):
    queue = deque([start])
    visited[start] = True
    cnt = 0
    while queue:
        v = queue.popleft()
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return cnt

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

max_cnt = 0
answer = []

for i in range(1, N+1):
    visited = [False for _ in range(N+1)]
    cnt = bfs(i, visited)
    if cnt == max_cnt:
        answer.append(i)
    elif cnt >= max_cnt:
        max_cnt = cnt
        answer = [i]

print(" ".join(map(str, answer)))