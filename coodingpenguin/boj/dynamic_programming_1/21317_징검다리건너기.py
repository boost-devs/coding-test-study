# 문제: [BOJ 21317] 징검다리 건너기
# 유형: 동적계획법
# 메모리/시간: 29200kb / 64ms

import sys

input = sys.stdin.readline


def fill_table(table):
    # 작은 점프와 큰 점프만 가능한 경우
    for i in range(2, n):
        table[i] = min(table[i - 1] + small[i - 1], table[i - 2] + large[i - 2])

    # 가장 큰 점프도 추가한 경우
    for i in range(n - 1, 2, -1):
        larger = table[i - 3] + k  # 가장 큰 점프시 소모 에너지
        # 소모 에너지가 기존보다 작다면
        if table[i] > larger:
            # i이후의 테이블 갱신
            table[i] = larger
            for j in range(i, n):
                table[j] = min(
                    table[j], table[j - 1] + small[j - 1], table[j - 2] + large[j - 2]
                )
    return table


def get_least_energy():
    # n이 3보다 작거나 같은 경우
    if n == 1:
        return 0
    elif n == 2:
        return small[0]
    elif n == 3:
        return min(small[0] + small[1], large[0])

    # n이 3보다 큰 경우
    table = [0] * n
    table[1] = small[0]
    table = fill_table(table)  # 테이블 채우기

    return table[-1]


n = int(input())  # 돌의 개수
small, large = [], []  # 작은 점프와 큰 점프 소모 에너지
for _ in range(n - 1):
    s, l = map(int, input().split())
    small.append(s)
    large.append(l)
k = int(input())  # 가장 큰 점프 소모 에너지

print(get_least_energy())
