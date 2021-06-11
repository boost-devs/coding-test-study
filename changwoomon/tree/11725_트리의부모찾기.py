# 11725번: 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725
# 메모리/시간: 49220KB / 420ms

import sys
from collections import deque

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())

tree = [[] for _ in range(N+1)]
parent = [0 for _ in range(N+1)]

for _ in range(N-1):
    start, end = map(int, input().split())
    tree[start].append(end)
    tree[end].append(start)

def bfs(start, parent):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for i in tree[node]:
            if parent[i] == 0:
                queue.append(i)
                parent[i] = node

bfs(1, parent)

for i in range(2, N+1):
    print(parent[i])