# 문제: [BOJ 13023] ABCDE
# 유형: DFS
# 메모리/시간: 31872KB / 3004ms
# 참고: https://velog.io/@nyanyanyong/알고리즘백준-ABCDE

import sys
from collections import defaultdict

input = sys.stdin.readline


def dfs(v, count):
    global result
    visited[v] = True
    # 깊이가 5라면, ABCDE 관계 성립
    if count == 5:
        result = 1
        return
    # 모든 인접 노드에 대해서
    for i in links[v]:
        # 방문하지 않았다면
        if not visited[i]:
            dfs(i, count + 1)  # 깊이 우선 탐색 수행
            visited[i] = False  # 수행 후 visited 복구


# 입력
n, m = map(int, input().split())  # 사람 수, 친구 관계의 수
links = defaultdict(list)  # 친구 관계
for _ in range(m):
    a, b = map(int, input().split())
    links[a].append(b)
    links[b].append(a)

visited = [False] * n  # 방문 여부

result = 0  # ABCDE 관계 존재 여부
# 모든 모드에 대하여
for i in range(n):
    dfs(i, 1)  # 깊이 우선 탐색 수행
    visited[i] = False  # 수행 후 visited 복구
    # ABCDE 관계가 있다면 탈출
    if result:
        break

# 출력
print(result)
