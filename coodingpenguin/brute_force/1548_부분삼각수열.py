# 문제: [BOJ 1548] 부분 삼각 수열
# 유형: 완전 탐색, 조합
# 메모리/시간: 29200kb / 84ms
# 참고: http://isukorea.com/blog/article/89

import sys
from itertools import combinations

input = sys.stdin.readline

def result(n:int, arr:list):
    # 수열 크기가 3이하인 경우
    if n < 3:
        return n    # 수열 크기만큼이 최대 길이
    combs = combinations(range(n), 3)
    max_length = 2  # 수열 최대 길이
    for a, b, c in combs:
        # 삼각 수열을 만족한다면
        if arr[a] + arr[b] > arr[c]:
            # b와 c 사이의 요소를 포함한 수열이 최대 수열
            max_length = max(max_length, c-b+2)
    return max_length

# 입력
n = int(input())    # 수열 길이
arr = list(map(int, input().split()))   # 수열
arr.sort()  # 오름차순 정렬

# 출력
print(result(n, arr))

