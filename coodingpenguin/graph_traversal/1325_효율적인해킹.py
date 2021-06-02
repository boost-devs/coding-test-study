# 문제: [BOJ 1325] 효율적인 해킹
# 유형: BFS
# 메모리/시간: 224332kb / 14360ms (PyPy3)
# 참고: https://pacific-ocean.tistory.com/337

import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def bfs(start):
    visited = [False] * (n + 1)
    visited[start] = True
    queue = deque([start])
    count = 1  # 카운트 초기화
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                count += 1  # 방문 할 때마다 1씩 증가
    return count


# 입력
n, m = map(int, input().split())  # 노드, 간선의 수
graph = defaultdict(list)  # 연결 리스트
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

result = []
max_count = -1
for i in range(1, n + 1):
    count = bfs(i)  # i 노드의 감염 수
    # 최대값과 같다면 추가
    if max_count == count:
        result.append(i)
    # 최대값보다 더 높은 값이 나오면 초기화
    if max_count < count:
        max_count = count
        result = [i]

# 출력
print(*result)
