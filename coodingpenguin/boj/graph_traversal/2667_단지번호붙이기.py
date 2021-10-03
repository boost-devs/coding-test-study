# 문제: [BOJ 2667] 단지번호붙이기
# 유형: DFS
# 메모리/시간: 29140kb / 72ms

import sys

input = sys.stdin.readline
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우하좌상


def dfs(y, x, count):
    visited[y][x] = True  # 방문 체크
    count += 1  # 방문 노드 수 +1
    # 모든 방향에 대해 탐색
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        # 지도 범위 내에 있고
        if (0 <= nx < n) and (0 <= ny < n):
            # 방문 하지 않았고 집이 있을 때
            if not visited[ny][nx] and arr[ny][nx] == "1":
                # 해당 노드에서 재탐색 및 count 갱신
                count = dfs(ny, nx, count)
    return count


# 입력
n = int(input())  # 지도의 크기
arr = [list(input().rstrip()) for _ in range(n)]  # 지도

visited = [[False] * n for _ in range(n)]  # 방문 여부
result = []  # 단지별 집의 수

for i in range(n):
    for j in range(n):
        # 집이 없거나 방문한 곳이면 패스
        if arr[i][j] == "0" or visited[i][j]:
            continue
        # 깊이 우선 탐색
        count = dfs(i, j, 0)
        # 단지의 집의 개수 추가
        result.append(count)

# 오름차순 정렬
result.sort()

# 출력
print(len(result))
for i in result:
    print(i)
