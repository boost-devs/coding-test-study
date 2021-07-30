# https://www.acmicpc.net/problem/15961
# 회전 초밥
# 179712 KB / 1184 ms


import sys
from collections import Counter


input = sys.stdin.readline

N, _, k, c = map(int, input().split())
on_belt = [int(input()) for _ in range(N)]

on_belt += on_belt[:k - 1]
k_counter = Counter(on_belt[:k])
unique_in_k = set(on_belt[:k])
max_num = len(unique_in_k) + int(c not in unique_in_k)
for f in range(N - 1):
    if max_num == k + 1:
        break
    
    n = f + k
    k_counter[on_belt[f]] -= 1
    k_counter[on_belt[n]] = k_counter.get(on_belt[n], 0) + 1
    if k_counter[on_belt[f]] == 0:
        unique_in_k.remove(on_belt[f])
    if k_counter[on_belt[n]] == 1:
        unique_in_k.add(on_belt[n])
    
    max_num = max(
        max_num, 
        len(unique_in_k) + int(c not in unique_in_k)
    )

print(max_num)
