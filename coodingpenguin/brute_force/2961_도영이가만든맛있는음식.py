# 문제: [BOJ 2961] 도영이가 만든 맛있는 음식
# 유형: 비트마스크, 완전 탐색
# 메모리/시간: 29200kb / 72ms

import sys

input = sys.stdin.readline


def result(n: int, foods: list):
    min_diff = sys.maxsize  # 신맛과 쓴맛의 최소 차
    # 모든 조합에 대해서
    for i in range(1, 1 << n):
        sour, sweet = 1, 0  # 신맛 총곱, 쓴맛 총합
        for j in range(n):
            if i & 1 << j:
                sour *= foods[j][0]
                sweet += foods[j][1]
        min_diff = min(min_diff, abs(sour - sweet))  # 작은 값으로 갱신
    return min_diff


# 입력
n = int(input())  # 재료 수
foods = [list(map(int, input().split())) for _ in range(n)]  # 음식별 신맛, 쓴맛

# 출력
print(result(n, foods))
