import sys
from collections import deque

input = sys.stdin.readline
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def migrate(arr, countries, total):
    avg = total // len(countries)
    for y, x in countries:
        arr[y][x] = avg


def bfs(sy, sx, n, arr, l, r, visited):
    total = arr[sy][sx]
    visited[sy][sx] = True
    countries = [(sy, sx)]
    queue = deque([(sy, sx)])
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if (
                0 <= ny < n
                and 0 <= nx < n
                and not visited[ny][nx]
                and l <= abs(arr[y][x] - arr[ny][nx]) <= r
            ):
                visited[ny][nx] = True
                total += arr[ny][nx]
                queue.append((ny, nx))
                countries.append((ny, nx))
    if len(countries) > 1:
        migrate(arr, countries, total)
        return True, visited
    return False, visited


def get_total_migration_days(n, l, r, arr):
    days = 0
    while True:
        visited = [[False] * n for _ in range(n)]
        any_migrated = False
        for y in range(n):
            for x in range(n):
                if not visited[y][x]:
                    is_migrated, visited = bfs(y, x, n, arr, l, r, visited)
                    any_migrated = any_migrated or is_migrated
        if any_migrated:
            days += 1
        else:
            return days


n, l, r = map(int, input().split())  # 크기, 인구차 하한선/상한선
arr = [list(map(int, input().split())) for _ in range(n)]  # 나라별 인구수

print(get_total_migration_days(n, l, r, arr))
