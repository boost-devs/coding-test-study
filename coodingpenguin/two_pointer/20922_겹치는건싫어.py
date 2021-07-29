# 문제: [BOJ 21921] 블로그
# 유형: 슬라이딩 윈도우
# 메모리/시간: 58192kb / 184ms
# 참고: https://www.acmicpc.net/source/31250776

import sys
from collections import defaultdict

input = sys.stdin.readline


def result(n, k, arr):
    counter = defaultdict(int)  # 숫자 카운터
    start, end = 0, 0  # 시작, 끝 포인터
    max_length = -1  # 최장 길이
    # 끝 포인터가 범위 내이고
    while end < n:
        # end 위치에 있는 요소의 개수가 k개 미만이라면
        if counter.get(arr[end], 0) < k:
            counter[arr[end]] += 1  # 끝 포인터 요소 카운트 증가
            end += 1  # 끝 포인터 이동
        # k개 이상이라면
        else:
            max_length = max(max_length, end - start)  # 최장 길이 갱신
            counter[arr[start]] -= 1  # 시작 포인터 요소 카운트 감소
            start += 1  # 시작 포인터 이동

    # 최장 길이 마지막으로 갱신
    return max(max_length, end - start)


N, K = map(int, input().split())  # 수열 길이, 중복 허용 개수
arr = list(map(int, input().split()))  # 수열

print(result(N, K, arr))
