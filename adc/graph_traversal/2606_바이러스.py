# 2606번: 바이러스
# https://www.acmicpc.net/problem/2606

import sys

input = sys.stdin.readline

# DFS 메서드 정의
def dfs(v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    # print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)
    return visited

N = int(input())
L = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(L):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [False for _ in range(N+1)]
answer = sum(dfs(1, visited)) - 1
print(answer)