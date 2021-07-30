# 문제: [BOJ 2470] 두 용액
# 유형: 투 포인터
# 메모리/시간: 189460kb / 4488ms
# 참고: https://ansohxxn.github.io/boj/2470/

import sys

input = sys.stdin.readline


def result(n: int, arr: list) -> tuple:
    # 용액수가 2이면
    if n == 2:
        # 두 용액의 합을 반환
        return arr[0], arr[1]
    start, end = 0, n - 1  # 포인터
    zero_water = int(2e9)  # 최소 특성값
    a, b = 0, 0  # 최소일 때의 두 용액 특성값
    while start < end:
        water = arr[start] + arr[end]  # 용액 혼합
        # 최솟값보다 더 작다면
        if zero_water > abs(water):
            # 최소 특성값 및 두 용액 특성값 갱신
            zero_water = abs(water)
            a, b = arr[start], arr[end]
            # 최소인 0이라면
            if not water:
                # 바로 두 용액 반환
                return a, b
        # 특성값 합이 0보다 작다면
        if water < 0:
            # start 포인터를 증가시켜 water도 증가시킴
            start += 1
        # 0보다 크거나 같다면
        else:
            # end 포인터를 감소시켜 water도 감소시킴
            end -= 1
    return a, b


# 입력
n = int(input())  # 전체 용액수
arr = sorted(map(int, input().split()))  # 정렬된 용액 특성값

# 출력
print(*result(n, arr))
