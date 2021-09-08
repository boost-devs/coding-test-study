# 문제: [BOJ 16234] 인구 이동
# 유형: 시뮬레이션, 구현
# 메모리/시간: 33032kb / 7508ms, 165768kb / 2936ms (PyPy3)

import sys
from collections import deque

input = sys.stdin.readline
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def migrate(arr, countries, total):
    avg = total // len(countries)  # 평균 인구수
    for y, x in countries:
        arr[y][x] = avg


def bfs(sy, sx, n, arr, l, r, visited):
    total = arr[sy][sx]  # 연합 나라의 총 인구수
    visited[sy][sx] = True  # 방문 체크
    countries = [(sy, sx)]  # 연합 나라 리스트
    queue = deque([(sy, sx)])  # 우선순위 큐
    while queue:
        y, x = queue.popleft()
        # 모든 방향에 대해서
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if (
                0 <= ny < n  # 격자판 내에 있고
                and 0 <= nx < n
                and not visited[ny][nx]  # 방문한 적이 없고
                and l <= abs(arr[y][x] - arr[ny][nx]) <= r  # 인구 차이가 l명 이상 r명 이하라면
            ):
                visited[ny][nx] = True  # 방문 여부를 체크
                total += arr[ny][nx]  # 총 인구수 증가
                queue.append((ny, nx))  # 우선순위 큐에 추가
                countries.append((ny, nx))  # 연합 나라에 추가
    # 연합 나라의 수가 1보다 크다면
    if len(countries) > 1:
        # 인구 이동을 시킨다
        migrate(arr, countries, total)
        return True, visited
    return False, visited


def get_total_migration_days(n, l, r, arr):
    days = 0  # 인구이동 발생 일수
    while True:
        visited = [[False] * n for _ in range(n)]  # 방문 여부
        any_migrated = False  # 이동 여부
        for y in range(n):
            for x in range(n):
                # 방문한 적이 없다면
                if not visited[y][x]:
                    # 너비 우선 탐색을 수행하고
                    is_migrated, visited = bfs(y, x, n, arr, l, r, visited)
                    # 이동 여부를 갱신한다
                    any_migrated = any_migrated or is_migrated
        # 이동이 한 번이라도 있었다면
        if any_migrated:
            days += 1  # 발생 일수를 1 증가시킨다
        # 아니라면
        else:
            return days  # 종료한다


n, l, r = map(int, input().split())  # 크기, 인구차 하한선/상한선
arr = [list(map(int, input().split())) for _ in range(n)]  # 나라별 인구수

print(get_total_migration_days(n, l, r, arr))  # 인구이동 발생 일수
