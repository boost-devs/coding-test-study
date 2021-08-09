# 문제: [BOJ 9079] 동전 게임
# 유형: 비트마스크, 완전 탐색
# 메모리/시간: 29200kb / 68ms

import sys

input = sys.stdin.readline
INF = int(1e9)
flips = [7, 56, 73, 84, 146, 273, 292, 448]  # 뒤집기 연산 비트 리스트


def get_minimum_number_of_operations(arr):
    result = INF  # 최소 연산 수
    # 가능한 모든 연산의 경우의 수에 대하여
    for flip in range(2 ** 8):
        flip_bits = bin(flip)[2:].zfill(8)  # 연산을 비트로 변환
        number_of_one = flip_bits.count("1")  # 1인 비트수
        # 최소 연산 수보다 연산 횟수가 크다면
        if number_of_one > result:
            continue  # 패스
        arr_to_int = int(arr, 2)  # 비트를 정수로 변환
        for i in range(8):
            # 1인 경우만 연산 수행
            if flip_bits[i] == "1":
                arr_to_int ^= flips[i]

        # 연산 결과가 모두 0이거나 1인 경우
        if arr_to_int in (0, 511):
            result = number_of_one  # 최소 연산 수 갱신
    if result == INF:
        return -1  # 모두 같은 면이 보이도록 할 수 없음
    return result


t = int(input())  # 테스트 케이스 수
for _ in range(t):
    arr = ""  # 배열을 1차원 비트로 변환
    for _ in range(3):
        arr += "".join(["1" if i == "T" else "0" for i in input().split()])
    print(get_minimum_number_of_operations(arr))
