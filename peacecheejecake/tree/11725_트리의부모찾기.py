# https://www.acmicpc.net/problem/11725
# 트리의 부모 찾기

from collections import defaultdict, deque

N = int(input())
graph = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parents = dict()
visited = {v: (True if v == 1 else False) for v in range(1, N + 1)}
queue = deque([1])
while queue:
    v = queue.popleft()
    for n in graph[v]:
        if not visited[n]:
            parents[n] = v
            queue.append(n)
            visited[n] = True

for node in range(2, N + 1):
    print(parents[node])
