# 문제: [BOJ 16937] 두 스티커
# 유형: 완전 탐색
# 메모리/시간: 29452kb / 96ms

import sys
from itertools import combinations

input = sys.stdin.readline

# 입력
h, w = map(int, input().split())  # 모눈종이 세로, 가로
n = int(input())  # 스티커 수
stickers = [list(map(int, input().split())) for _ in range(n)]  # 스티커 별 크기

combs = list(combinations(range(n), 2))  # 스티커 조합 경우의 수
max_area = -1  # 두 스티커 넓이 최댓값
for i, j in combs:
    _r1, _c1 = stickers[i]
    _r2, _c2 = stickers[j]
    twos = [
        (_r1, _c1, _r2, _c2),  # 기본, 기본
        (_r1, _c1, _c2, _r2),  # 기본, 회전
        (_c1, _r1, _r2, _c2),  # 회전, 기본
        (_c1, _r1, _c2, _r2),  # 회전, 회전
    ]
    for r1, c1, r2, c2 in twos:
        # 세로를 접하는 경우
        if max(r1, r2) <= h and c1 + c2 <= w:
            max_area = max(max_area, r1 * c1 + r2 * c2)
        # 가로를 접하는 경우
        if r1 + r2 <= h and max(c1, c2) <= w:
            max_area = max(max_area, r1 * c1 + r2 * c2)

# 출력
if max_area == -1:
    print(0)
else:
    print(max_area)
