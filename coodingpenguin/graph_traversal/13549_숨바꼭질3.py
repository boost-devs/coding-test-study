# 문제: [BOJ 13549] 숨바꼭질3
# 유형: BFS
# 메모리/시간: 	35412kb / 188ms
# 참고:
# 	- https://velog.io/@aonee/백준-boj-13549-숨바꼭질3-파이썬
# 	- https://www.acmicpc.net/board/view/38887#comment-69010
# 	- https://www.acmicpc.net/board/view/54741

import sys
from collections import deque

input = sys.stdin.readline
MAX = 100000  # 최대 길이


def bfs(start):
    queue = deque([start])
    cost[start] = 0
    while queue:
        # 도착치 k까지의 최소 시간이 갱신됐다면
        if cost[k] != -1:
            return
        v = queue.popleft()
        # 순간이동, 앞/뒤 이동 수행 (우선 순위 있음)
        for nv, nt in zip([v * 2, v - 1, v + 1], [0, 1, 1]):
            # 범위에 벗어나지 않고
            if 0 <= nv <= MAX:
                # 최소 시간이 갱신되지 않았다면
                if cost[nv] == -1:
                    cost[nv] = cost[v] + nt  # 최소시간 갱신
                    queue.append(nv)  # 큐 삽입


# 입력
n, k = map(int, input().split())  # 수빈 위치, 동생 위치
cost = [-1] * (MAX + 1)  # n에서 임의 위치까지 걸리는 최소 시간

# 너비 우선 탐색
bfs(n)

# 출력
print(cost[k])
