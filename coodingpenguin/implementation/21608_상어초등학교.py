# 문제: [BOJ 21608] 상어 초등학교
# 유형: 구현
# 메모리/시간: 32224kb / 284ms

import sys
from collections import Counter

input = sys.stdin.readline
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 하우상좌


def get_most_commons(lst):
    most_commons = []  # 최대 카운트를 가진 좌표들 리스트
    MAX_COUNT = lst[0][0]  # 최대 카운트
    for count, *position in lst:
        if count == MAX_COUNT:
            most_commons.append(position)
    return most_commons


def set_position(student, position):
    y, x = position
    table[y][x] = student  # 학생 자리에 배치
    positions[student] = (y, x)  # 학생 위치 저장


def find_most_likes(likes):
    seats = []
    for y in range(n):
        for x in range(n):
            # 자리가 있는 곳이면 패스
            if table[y][x]:
                continue
            count = 0  # 좋아하는 사람 수
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                # 범위 밖이면 패스
                if (ny < 0 or ny >= n) or (nx < 0 or nx >= n):
                    continue
                # 좋아하는 사람이 있다면
                if table[ny][nx] in likes:
                    count += 1  # 카운트 +1
            seats.append((count, y, x))
    # 카운트는 큰 순, 위치는 작은 순으로 정렬
    seats.sort(key=lambda x: (-x[0], x[1], x[2]))
    return get_most_commons(seats)


def find_most_blanks(most_likes):
    seats = []
    for y, x in most_likes:
        count = 0  # 빈칸 개수
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            # 범위 밖이면 패스
            if (ny < 0 or ny >= n) or (nx < 0 or nx >= n):
                continue
            # 빈 자리라면
            if not table[ny][nx]:
                count += 1  # 카운트 +1
        seats.append((count, y, x))
    # 카운트는 큰 순, 위치는 작은 순으로 정렬
    seats.sort(key=lambda x: (-x[0], x[1], x[2]))
    return get_most_commons(seats)


def calculate_satisfaction():
    score = 0  # 만족도
    for student, likes in survey.items():
        y, x = positions[student]  # 학생 위치
        count = 0  # 좋아하는 사람 수
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            # 범위 내면 패스
            if (ny < 0 or ny >= n) or (nx < 0 or nx >= n):
                continue
            # 좋아하는 사람이 인접해 있다면
            if table[ny][nx] in likes:
                count += 1  # 카운트 +1
        # 좋아하는 사람이 있는 경우만
        if count:
            score += 10 ** (count - 1)  # 만족도 갱신
    return score


n = int(input())  # 학생 수
survey = {}  # 학생 별 좋아하는 학생 목록
for _ in range(n * n):
    student, *likes = map(int, input().split())
    survey[student] = set(likes)

table = [[0] * n for _ in range(n)]  # 자리
positions = {}  # 학생 위치

for student, likes in survey.items():
    # 조건 1. 좋아하는 학생이 많이 인접한 자리로 지정
    like_seats = find_most_likes(likes)
    if len(like_seats) == 1:
        set_position(student, like_seats.pop(0))
        continue
    # 조건2, 3. 인접한 칸 중 빈 칸이 많은 자리로 지정
    blank_seats = find_most_blanks(like_seats)
    set_position(student, blank_seats.pop(0))

satisfaction = calculate_satisfaction()  # 만족도 계산
print(satisfaction)
