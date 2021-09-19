# 문제: [BOJ 1890] 점프
# 유형: 동적계획법
# 메모리/시간: 29200kb / 68ms

import sys

input = sys.stdin.readline


def find_number_of_path(n, arr):
    # 테이블 생성 및 초기화
    table = [[0] * n for _ in range(n)]
    table[0][0] = 1

    for y in range(n):
        for x in range(n):
            # 도착지점이면 종료
            if y == x == n - 1:
                break
            # 갈 수 있는 곳이라면
            if table[y][x]:
                ny, nx = y + arr[y][x], x + arr[y][x]  # 새로운 위치
                # 범위 내라면 테이블 갱신
                if 0 <= ny < n:
                    table[ny][x] += table[y][x]
                if 0 <= nx < n:
                    table[y][nx] += table[y][x]
    return table[-1][-1]


n = int(input())  # 게임 판 크기
arr = []  # 게임 판
for _ in range(n):
    arr.append(list(map(int, input().split())))

print(find_number_of_path(n, arr))
