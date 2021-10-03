# 문제: [BOJ 1969] DNA
# 유형: 완전 탐색
# 메모리/시간: 31780kb / 100ms

import sys
from collections import Counter

input = sys.stdin.readline


def get_shortest_distance(dna: list, size: int, length: int) -> tuple:
    min_ham_dist = 0  # 해밍 거리 합 최솟값
    min_ham_dna = ""  # 일 때의 DNA 문자열
    for letters in zip(*dna):
        # 개수는 내림차순, 문자는 오름차순으로 정렬
        counter = sorted(Counter(letters).items(), key=lambda x: (-x[1], x[0]))
        # 해밍 거리 최솟값과 문자열 갱신
        min_ham_dna += counter[0][0]
        min_ham_dist += size - counter[0][1]

    return min_ham_dna, min_ham_dist


# 입력
n, m = map(int, input().split())  # DNA 수, 문자열 길이
dna = [input().rstrip() for _ in range(n)]  # 문자열 배열

# 출력
min_ham_dna, min_ham_dist = get_shortest_distance(dna, n, m)
print(min_ham_dna)
print(min_ham_dist)
