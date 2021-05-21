# 문제: [BOJ 7569] 토마토
# 유형: BFS
# 메모리/시간: 88004kb / 2660ms

import sys
from collections import deque

input = sys.stdin.readline
direction = [
    (0, 0, 1),  # 오른
    (0, -1, 0),  # 뒤
    (0, 0, -1),  # 왼
    (0, 1, 0),  # 앞
    (1, 0, 0),  # 위
    (-1, 0, 0),  # 아래
]


def bfs(pos):
    queue = deque(pos)
    count = -1  # 최소 날짜
    while queue:
        q_size = len(queue)
        # 큐에 있는 모든 노드에 대해 탐색
        for _ in range(q_size):
            z, y, x = queue.popleft()
            for dz, dy, dx in direction:
                nz, ny, nx = z + dz, y + dy, x + dx
                # 상자를 벗어나지 않고
                if (0 <= nz < h) and (0 <= ny < n) and (0 <= nx < m):
                    # 토마토가 익지 않았다면
                    if arr[nz][ny][nx] == "0":
                        arr[nz][ny][nx] = "1"  # 익히기
                        queue.append((nz, ny, nx))  # 큐에 삽입
        count += 1
    return count


def check_ripe(arr):
    # 익지 않은 토마토가 있는지 체크
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == "0":
                    return False
    return True


# 입력
m, n, h = map(int, input().split())  # 상자의 가로, 세로, 높이
arr = []  # 상자의 토마토 정보
for _ in range(h):
    arr.append([input().split() for _ in range(n)])

# 토마토가 있는 위치 추출
pos = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == "1":
                pos.append((i, j, k))

# 너비 우선 탐색
count = bfs(pos)
# 익지 않은 것이 있다면
if not check_ripe(arr):
    count = -1

# 출력
print(count)
