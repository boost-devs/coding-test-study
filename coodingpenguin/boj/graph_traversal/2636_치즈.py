# 문제: [BOJ 2636] 치즈
# 유형: BFS
# 메모리/시간: 32748kb / 120ms

import sys
from collections import deque

input = sys.stdin.readline
direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 우하좌상


def count_cheese():
    count = 0  # 치즈 개수
    for i in range(h):
        for j in range(w):
            if arr[i][j] == "1":
                count += 1
    return count


def bfs(sy, sx):
    queue = deque([(sy, sx)])
    visited[sy][sx] = True  # 시작 노드 방문 처리
    count = 0  # 녹을 치즈 개수
    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            # 판 안에 있고
            if (0 <= ny < h) and (0 <= nx < w):
                # 방문하지 않았다면
                if not visited[ny][nx]:
                    visited[ny][nx] = True  # 방문 처리
                    # 빈 공간인 경우
                    if arr[ny][nx] == "0":
                        queue.append((ny, nx))  # 큐에 삽입
                    # 치즈인 경우
                    else:
                        count += 1  # 치즈 개수 +1
                        arr[ny][nx] = "0"  # 치즈 녹이기
    return count


# 입력
h, w = map(int, input().split())  # 판의 세로, 가로
arr = [input().split() for _ in range(h)]

total = count_cheese()  # 총 치즈 개수
times = 0  # 다 녹는 데까지 걸린 시간
while True:
    visited = [[False] * w for _ in range(h)]  # 방문 여부
    times += 1  # 시간 +1

    # 너비 우선 탐색
    melt = bfs(0, 0)  # 녹은 치즈 개수

    # 남은 치즈와 녹은 치즈 개수가 같다면
    if total == melt:
        # 루프를 빠져나오기
        break
    # 아니라면 총 치즈 개수에서 빼기
    total -= melt

# 출력
print(times)
print(total)
