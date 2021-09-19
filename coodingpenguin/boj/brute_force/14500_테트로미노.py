# 문제: [BOJ 14500] 테트로미노
# 유형: 완전 탐색, 구현
# 메모리/시간: 35012kb / 4408ms, 127016kb / 504ms (PyPy3)

import sys

input = sys.stdin.readline

# 가능한 테트로미노 종류
tetronominoes = [
    [[(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 0), (1, 0), (2, 0), (3, 0)]],  # 하늘색
    [[(0, 0), (0, 1), (1, 0), (1, 1)]],  # 노랑색
    [
        [(0, 0), (1, 0), (2, 0), (2, 1)],
        [(1, 0), (1, 1), (1, 2), (0, 2)],
        [(0, 0), (0, 1), (1, 1), (2, 1)],
        [(0, 0), (0, 1), (0, 2), (1, 0)],
        [(0, 1), (1, 1), (2, 1), (2, 0)],
        [(0, 0), (1, 0), (1, 1), (1, 2)],
        [(0, 0), (0, 1), (1, 0), (2, 0)],
        [(0, 0), (0, 1), (0, 2), (1, 2)],
    ],  # 주황색
    [
        [(0, 0), (1, 0), (1, 1), (2, 1)],
        [(1, 0), (1, 1), (0, 1), (0, 2)],
        [(0, 1), (1, 1), (1, 0), (2, 0)],
        [(0, 0), (0, 1), (1, 1), (1, 2)],
    ],  #  초록색
    [
        [(0, 0), (0, 1), (0, 2), (1, 1)],
        [(1, 0), (1, 1), (1, 2), (0, 1)],
        [(0, 0), (1, 0), (2, 0), (1, 1)],
        [(1, 0), (0, 1), (1, 1), (2, 1)],
    ],  # 분홍색
]


def get_tetromino_max_sum(n, m, arr, pos):
    max_total_sum = -1  # 현재 테트로미노에 대한 수합 최댓값
    # 종이 위에 모든 위치에 대해서
    for y in range(n):
        for x in range(m):
            total_sum = 0  # 수합
            is_abnormal = False  # 비정상 종료 플래그
            for dy, dx in pos:
                ny, nx = y + dy, x + dx
                # 테트로미노가 종이 밖으로 나온다면
                if (ny < 0 or ny >= n) or (nx < 0 or nx >= m):
                    is_abnormal = True  # 비정상 종료 표시
                    break
                total_sum += arr[ny][nx]
            # 비정상 종료가 아닌 경우에만
            if not is_abnormal:
                max_total_sum = max(max_total_sum, total_sum)  # 수합 최댓값 갱신
    return max_total_sum


def get_maximum_sum(n, m, arr):
    maximum_sum = -1  # 수합의 최댓값
    # 가능한 모든 테트로미노 종류에 대하여
    for tetronomino in tetronominoes:
        for case in tetronomino:
            # 종이 위에 놓고 stride=1로 순회하면서 최댓값 갱신
            maximum_sum = max(maximum_sum, get_tetromino_max_sum(n, m, arr, case))
    return maximum_sum


# 입력
n, m = map(int, input().split())  # 종이 세로, 가로 길이
arr = [list(map(int, input().split())) for _ in range(n)]  # 종이 위 숫자 배열

# 출력
print(get_maximum_sum(n, m, arr))
