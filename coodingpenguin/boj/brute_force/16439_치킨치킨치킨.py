# 문제: [BOJ 16439] 치킨치킨치킨
# 유형: 완전 탐색
# 메모리/시간: 29452kb / 100ms

import sys
from itertools import combinations

input = sys.stdin.readline

# 입력
n, m = map(int, input().split())  # 회원수, 치킨 종류수
tastes = [list(map(int, input().split())) for _ in range(n)]  # 회원별 치킨 선호도

max_taste_sum = -1  # 최대 만족도 합
combs = list(combinations(range(m), 3))  # 치킨 조합 경우의 수

# 모든 조합 경우의 수에 대해
for a, b, c in combs:
    # 주어진 치킨에서 회원별 선호도가 높은 치킨 선택
    taste_sum = sum([max(tastes[i][a], tastes[i][b], tastes[i][c]) for i in range(n)])
    # 만족도합이 기존보다 크다면 갱신
    max_taste_sum = max(max_taste_sum, taste_sum)

# 출력
print(max_taste_sum)
