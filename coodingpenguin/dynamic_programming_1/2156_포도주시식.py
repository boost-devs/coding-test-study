# 문제: [BOJ 2156] 포도주 시식
# 유형: 동적계획법
# 메모리/시간: 29708kb / 84ms

import sys

input = sys.stdin.readline


def result(n, wines):
    # 3개 미만이면
    if n < 3:
        # 다 마신다
        return sum(wines)
    # 3개 이상이면 테이블 생성
    table = [0] * (n + 1)
    table[1] = wines[1]
    table[2] = wines[1] + wines[2]

    for i in range(3, n + 1):
        table[i] = max(
            table[i - 1],  # 경우 1. 안 마신다
            max(  # 경우 2. 마신다
                table[i - 2] + wines[i],  # 경우 2-1. 전전과 현재 거를 마신다
                table[i - 3] + wines[i - 1] + wines[i],  # 경우 2-2. 전전전과 전, 현재거를 마신다
            ),
        )
    return table[n]


n = int(input())  # 포도주 잔의 개수
wines = [0] + [int(input()) for _ in range(n)]  # 포도주
print(result(n, wines))
