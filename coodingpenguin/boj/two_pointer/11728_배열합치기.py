# 문제: [BOJ 11728] 배열 합치기
# 유형: 포인터, 병합 정렬
# 메모리/시간: 184096kb / 2168ms

import sys

input = sys.stdin.readline


def merge_sort(arr_a, arr_b):
    pa, pb = 0, 0  # 배열 A, B의 포인터
    sorted_arr = []  # 정렬된 배열

    while pa < len(arr_a) and pb < len(arr_b):
        if arr_a[pa] <= arr_b[pb]:
            sorted_arr.append(arr_a[pa])
            pa += 1  # 포인터 이동
        else:
            sorted_arr.append(arr_b[pb])
            pb += 1  # 포인터 이동

    # 남은 요소 추가
    if pa < len(arr_a):
        sorted_arr += arr_a[pa:]
    if pb < len(arr_b):
        sorted_arr += arr_b[pb:]
    return sorted_arr


N, M = map(int, input().split())  # 배열 A, B의 크기
A = list(map(int, input().split()))  # 배열 A
B = list(map(int, input().split()))  # 배열 B

# 병합 정렬
print(*merge_sort(A, B))
