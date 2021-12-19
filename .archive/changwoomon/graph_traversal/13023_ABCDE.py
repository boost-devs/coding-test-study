###### 13023번: ABCDE
# https://www.acmicpc.net/problem/13023
# 메모리/시간: 29452KB / 3328ms

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
visited = [False] * N

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v, cnt):
    global answer
    visited[v] = True
    if cnt >= 4:
        answer = True
        return None
    for x in graph[v]:
        if not visited[x]:
            dfs(x, cnt+1)
            visited[x] = False

answer = False
for v in range(N):
    dfs(v, 0)
    visited[v] = False
    if answer:
        break

print(int(answer))