###### 18511번: 큰 수 구성하기
# https://www.acmicpc.net/problem/18511
# 메모리/시간: 36916KB / 104ms

import sys
from itertools import product

input = sys.stdin.readline

N, K = map(int, input().split())

K_set = [0] + list(map(int, input().split()))

for k in sorted(product(K_set, repeat=len(str(N))), reverse=True):
    if 0 in k[1:]:
        continue
    answer = int("".join(map(str, k)))
    if N >= answer:
        print(answer)
        break