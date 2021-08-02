# 문제: [BOJ 15961] 회전 초밥
# 유형: 슬라이딩 윈도우
# 메모리/시간: 40916kb / 144ms
# 참고: https://ryu-e.tistory.com/33

import sys
from collections import defaultdict

input = sys.stdin.readline

# 입력
n, d, k, c = map(int, input().split())  # 접시수, 초밥수, 연속수, 쿠폰번호
arr = [int(input()) for _ in range(n)]  # 회전 초밥
arr = arr * 2  # 원형 테이블

counter = defaultdict(int)  # 초밥 종류별 개수
counter[c] += 1  # 무료 초밥 미리 추가

start, end = 0, 0
max_count = 0  # 최대 가짓수

# 첫 k만큼 시식
while end < k:
    counter[arr[end]] += 1
    end += 1

# 한 바퀴를 다 돌때까지
while start < n:
    max_count = max(max_count, len(counter))  # 최대 가짓수 갱신

    # start, end 포인터 앞으로 이동
    counter[arr[start]] -= 1
    if not counter[arr[start]]:
        del counter[arr[start]]
    start += 1
    counter[arr[end]] += 1
    end += 1

# 출력
print(max_count)
