###### 1068번: 트리
# https://www.acmicpc.net/problem/1068
# 메모리/시간: 31780KB / 92ms

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
parents = list(map(int, input().split()))
del_node = int(input())

tree = [[] for _ in range(N)]

for i, par in enumerate(parents):
    if par != -1:
        tree[par].append(i)

for i, x in enumerate(tree):
    tree[i] = set(x)

def bfs(start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in tree[v]:
            if (not visited[i]):
                queue.append(i)
                visited[i] = True

visited = [False for _ in range(N)]

bfs(del_node, visited)

cnt = 0

for x, b in zip(tree, visited):
    if len(x) == 0 and not b:
        cnt += 1

for x, b in zip(tree, visited):
    if x == {del_node}:
        cnt += 1

print(cnt)