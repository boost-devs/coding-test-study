###### 20922번: 겹치는 건 싫어
# https://www.acmicpc.net/problem/20922
# 메모리/시간: 54196KB / 416ms

import sys
from collections import defaultdict

input = sys.stdin.readline

N, K = map(int, input().split())

array = list(map(int, input().split()))

cnt = defaultdict(int)

left, right = 0, 0
answer = 0

while (right < N):
    if cnt[array[right]] < K:
        cnt[array[right]] += 1
        right += 1
    else:
        cnt[array[left]] -= 1
        left += 1
    answer = max(answer, right-left)

print(answer)