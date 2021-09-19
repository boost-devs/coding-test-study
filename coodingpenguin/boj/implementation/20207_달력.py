# 문제: [BOJ 20207] 달력
# 유형: 구현
# 메모리/시간: 29200kb / 112ms

import sys

input = sys.stdin.readline

n = int(input())  # 일정 개수
calendar = [0] * 366  # 날짜별 일정 개수
MIN, MAX = 365, 1  # 최소, 최대 날짜
for _ in range(n):
    s, e = map(int, input().split())  # 시작, 종료 날짜
    # 최소, 최대 날짜 갱신
    if s < MIN:
        MIN = s
    if e > MAX:
        MAX = e
    # 날짜별 일정 개수 세기
    for i in range(s, e + 1):
        calendar[i] += 1

area = 0  # 직사각형 넓이합
w, h = 0, 0  # 가로, 세로
for i in range(MIN, MAX + 1):
    # 날짜에 일정이 있다면
    if calendar[i]:
        # 직사각형 가로, 세로 갱신
        h = max(h, calendar[i])
        w += 1
    # 없다면
    else:
        # 지금까지 구한 가로, 세로로
        area += w * h  # 넓이 구하기
        w, h = 0, 0  # 가로, 세로 초기화

# 일정이 마지막 날까지 있다면
if h and w:
    area += w * h  # 넓이 추가

print(area)
