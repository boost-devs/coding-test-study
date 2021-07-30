# 문제: [BOJ 14719] 빗물
# 유형: 구현
# 메모리/시간: 29200kb / 68ms
# 참고: https://www.acmicpc.net/board/view/18534

import sys

input = sys.stdin.readline


def get_total_water(walls):
    # 블록 개수가 1개라면
    if len(walls) == 1:
        # 물은 고이지 않는다
        return 0
    total_water = 0  # 빗물 총량
    for i in range(1, len(walls) - 1):
        left = max(walls[:i])  # 왼쪽에서 가장 높은 블록
        right = max(walls[i + 1 :])  # 오른쪽에서 가장 높은 블록
        standard = min(left, right)  # 작은 것이 기준
        # 기준보다 높이가 낮다면
        if walls[i] <= standard:
            # 고인 물을 총량에 더해준다
            total_water += standard - walls[i]
    return total_water


h, w = map(int, input().split())  # 세로, 가로 길이
walls = list(map(int, input().split()))  # 블록들 높이

print(get_total_water(walls))  # 빗물 총량
