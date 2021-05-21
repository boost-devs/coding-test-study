# https://www.acmicpc.net/problem/1325
import sys
from collections import deque, defaultdict

def bfs(start):
    q = deque([start])
    visited[start] = True
    cnt = 1 # 시작점
    while q:
        v = q.popleft()
        for i in graph_dict[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1   # 자식 노드 하나당 ++
    return cnt

input = sys.stdin.readline
n, m = map(int, input().split())
graph_dict = defaultdict(list)
candi=set([])  # 부모 노드들 저장
for _ in range(m):
    s, e = map(int, input().split())
    graph_dict[e].append(s)
    candi.add(e)
result = []
_max = -10000000

for i in candi:
    visited=[False for _ in range(n+1)]
    infect = bfs(i)
    if _max == infect: # 값이 같으면 append
        result.append(i)
    if _max < infect:
        _max = infect
        result = [i] # 배열 초기화

print(*sorted(result))