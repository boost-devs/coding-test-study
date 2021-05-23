# 문제: [BOJ 5547] 일루미네이션
# 유형: BFS
# 메모리/시간: 31880kb / 108ms
# 참고: 샐리님🐤

import sys
from collections import deque

input = sys.stdin.readline

dir_even = [(-1, -1), (-1, 0), (0, 1), (1, 0), (1, -1), (0, -1)]  # y가 짝수일 때 방향
dir_odd = [(1, 1), (-1, 0), (0, 1), (1, 0), (-1, 1), (0, -1)]  # y가 홀수일 때 방향


def bfs(sy, sx):
    queue = deque([(sy, sx)])
    count = 0  # 벽 개수
    while queue:
        y, x = queue.popleft()
        visited[y][x] = True  # 방문 처리
        direction = dir_even if not y % 2 else dir_odd  # y에 따른 방향 설정
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            # 지도 안에 있고
            if (0 <= ny < h + 2) and (0 <= nx < w + 2):
                # 건물이 있다면
                if arr[ny][nx] == 1:
                    count += 1  # 변 개수 카운트
                # 방문하지 않은 건물이 없는 곳이라면
                if arr[ny][nx] == 0 and not visited[ny][nx]:
                    visited[ny][nx] = True  # 방문 처리
                    queue.append((ny, nx))  # 큐에 삽입
    return count


# 입력
w, h = map(int, input().split())  # 너비, 높이
arr = [[0] + list(map(int, input().split())) + [0] for _ in range(h)]  # 지도 + 패드

# 위쪽, 아래쪽 패드 넣기
arr.insert(0, [0] * (w + 2))
arr.append([0] * (w + 2))

# 방문여부
visited = [[0] * (w + 2) for _ in range(h + 2)]

# 너비 우선 탐색
count = bfs(0, 0)

# 출력
print(count)
