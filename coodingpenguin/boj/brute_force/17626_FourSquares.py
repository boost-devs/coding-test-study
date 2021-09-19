# 문제: [BOJ 17626] Four Squares
# 유형: 완전 탐색
# 메모리/시간: 29200kb / 100ms
# 참고: https://www.acmicpc.net/source/31631794

import sys

input = sys.stdin.readline


def is_squared(n):
    if int(n ** 0.5) ** 2 == n:
        return True
    return False


def get_least_sum(n):
    count = 4  # 제곱수 개수

    # n이 제곱수라면
    if is_squared(n):
        return 1

    for i in range(1, int(n ** 0.5) + 1):
        for j in range(1, i + 1):
            two_sum = i ** 2 + j ** 2
            # 두 수의 제곱 합이 n과 같다면
            if two_sum == n:
                return 2  # 최솟값이니 바로 반환
            # 두 수의 제곱 합이 n보다 작지만 그 차이가 제곱수라면
            if two_sum < n and is_squared(n - two_sum):
                count = 3  # 2인 경우가 있을 수도 있으니 반환하지 않음

    return count


n = int(input())
print(get_least_sum(n))
