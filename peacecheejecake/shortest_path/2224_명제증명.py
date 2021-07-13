# https://www.acmicpc.net/problem/2224
# 명제 증명
#

from collections import defaultdict, deque

n = int(input())
graph = defaultdict(set)
indegree = defaultdict(int)
conds = set()
for _ in range(n):
    p, q = input().split(' => ')
    graph[p].add(q)
    indegree[q] += 1
    conds.update({p, q})

queue = deque()
for p in conds:
    if indegree[p] == 0:
        queue.append(p)

while queue:
    p = queue.popleft()
    



queue = deque([list(graph)[0]])
visited = defaultdict(bool)
relations = set()
while queue:
    p = queue.popleft()
    for q in graph[p]:
        if not visited[p]:
            relations.add((p, q))
            queue.append(q)

for p, q in sorted(relations):
    print(f'{p} => {q}')
