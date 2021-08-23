# https://www.acmicpc.net/problem/21278
# 32032 KB / 3908 ms


from itertools import combinations
from collections import deque


def bfs(graph, dists, chicken):
    visited = [False] * len(dists)
    visited[chicken] = True
    dists[chicken] = 0
    queue = deque([chicken])
    while queue:
        b = queue.popleft()
        d = dists[b]
        for ngb in graph[b]:
            if not visited[ngb]:
                dists[ngb] = min(dists[ngb], d + 1)
                visited[ngb] = True
                queue.append(ngb)


N, M = map(int, input().split())
graph = [set() for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    graph[a].add(b)
    graph[b].add(a)

min_sum_dist = int(1e9)
cands = []
for p, q in combinations(range(N), 2):
    dists = [M] * N
    bfs(graph, dists, p)
    bfs(graph, dists, q)
    sum_dist = sum(dists)
    if sum_dist < min_sum_dist:
        min_sum_dist = sum_dist
        cands = [(p, q)]
    elif sum_dist == min_sum_dist:
        cands.append((p, q))

cands.sort()
p_min, q_min = cands[0]
print(p_min + 1, q_min + 1, min_sum_dist * 2)
