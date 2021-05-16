# 문제: [BOJ 16234] 인구 이동
# 유형: BFS
# 메모리/시간:	145604kb / 2216ms

import sys
from collections import deque

input = sys.stdin.readline
direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 우하좌상


def unite_country(countries, total):
    avg = total // len(countries)  # 인구이동 시 새로운 인구
    for y, x in countries:
        arr[y][x] = avg


def bfs(sy, sx):
    queue = deque([(sy, sx)])
    countries = [(sy, sx)]  # 연합 나라
    visited[sy][sx] = True  # 방문 처리
    total = 0  # 연합의 총 인구 수
    while queue:
        y, x = queue.popleft()
        total += arr[y][x]
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            # 지도 내에 있고
            if (0 <= ny < n) and (0 <= nx < n):
                diff = abs(arr[ny][nx] - arr[y][x])  # 두 나라의 인구 차
                # 방문하지 않았고 인구 차가 범위 내에 있다면
                if not visited[ny][nx] and (l <= diff <= r):
                    visited[ny][nx] = True  # 방문 처리
                    countries.append((ny, nx))  # 연합에 추가
                    queue.append((ny, nx))  # 큐에 삽입
    return countries, total


# 입력
n, l, r = map(int, input().split())  # 땅 크기, 이상, 이하
arr = [list(map(int, input().split())) for _ in range(n)]  # 지도

result = 0  # 인구 이동 횟수
while True:
    is_moved = False  # 인구 이동 여부
    visited = [[False] * n for _ in range(n)]  # 방문 여부
    for i in range(n):
        for j in range(n):
            # 방문하지 않은 나라라면
            if not visited[i][j]:
                # 너비우선탐색으로 연합 구하기
                countries, total = bfs(i, j)
                # 연합이 없다면 패스
                if len(countries) == 1:
                    continue
                # 연합이 있다면 인구 이동
                unite_country(countries, total)
                is_moved = True
    # 더이상의 인구이동이 없으면 끝
    if not is_moved:
        break
    result += 1

print(result)
