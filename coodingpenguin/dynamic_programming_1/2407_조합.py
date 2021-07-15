# 문제: [BOJ 2407] 조합
# 유형: 동적계획법
# 메모리/시간: 29200kb / 72ms

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
MAX = max(n, m) # n, m 중 최대값
prefix_mult = [1] * (MAX+1) # 구간곱
for i in range(2, MAX+1):
    prefix_mult[i] = prefix_mult[i-1] * i

print(prefix_mult[n]//prefix_mult[m]//prefix_mult[n-m])