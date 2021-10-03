# 문제: [BOJ 14501] 퇴사
# 유형: 동적계획법
# 메모리/시간: 29200kb / 72ms

import sys

input = sys.stdin.readline

n = int(input())  # 가능한 출근 수
pays = [list(map(int, input().split())) for _ in range(n)]  # 상담 일정 표

table = [0] * (n + 2)  # DP 테이블
for i in range(1, n + 1):
    time, pay = pays[i - 1]  # 걸리는 기간, 상담 금액
    max_pay = max(table[: i + 1])  # 현재까지의 최대 이익
    # 퇴사일을 초과하지 않는 경우
    if i + time <= n + 1:
        # 새로운 이익과 기존 이익 중 최댓값으로 갱신
        table[i + time] = max(max_pay + pay, table[i + time])

print(max(table))  # 최대 이익
