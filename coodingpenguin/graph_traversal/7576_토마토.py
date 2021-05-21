# 문제: [BOJ 7576] 토마토
# 유형: BFS
# 메모리/시간: 146508kb / 1824ms

import sys
from collections import deque

input = sys.stdin.readline
direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 우하좌상


def bfs(pos):
    queue = deque(pos)
    count = -1  # 최소 날짜
    while queue:
        q_size = len(queue)
        # 큐에 있는 모든 노드에 대해 탐색
        for _ in range(q_size):
            y, x = queue.popleft()
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                # 상자를 벗어나지 않고
                if (0 <= ny < n) and (0 <= nx < m):
                    # 토마토가 익지 않았다면
                    if arr[ny][nx] == "0":
                        arr[ny][nx] = "1"  # 익히기
                        queue.append((ny, nx))  # 큐에 삽입
        count += 1
    return count


def check_ripe(arr):
    # 익지 않은 토마토가 있는지 체크
    for i in range(n):
        for j in range(m):
            if arr[i][j] == "0":
                return False
    return True


# 입력
m, n = map(int, input().split())  # 상자의 가로, 세로
arr = [input().split() for _ in range(n)]  # 상자의 토마토 정보

# 토마토가 있는 위치 추출
pos = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == "1":
            pos.append((i, j))

# 너비 우선 탐색
count = bfs(pos)
# 익지 않은 것이 있다면
if not check_ripe(arr):
    count = -1

# 출력
print(count)
