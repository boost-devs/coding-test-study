###### 2839번: 설탕 배달
# https://www.acmicpc.net/problem/2839
# 메모리/시간: 29200KB / 72ms

import sys

input = sys.stdin.readline

N = int(input())

cnt = 0

while N >= 0:
    if N % 5 == 0:
        cnt += N // 5
        print(cnt)
        break
    N -= 3
    cnt += 1
else:
    print(-1)