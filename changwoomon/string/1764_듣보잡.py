###### 1764번: 듣보잡
# https://www.acmicpc.net/problem/1764
# 메모리/시간: 41748KB / 128ms

import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

dont_hear = set()
dont_see = set()

for _ in range(N):
    dont_hear.add(input().rstrip())

for _ in range(M):
    dont_see.add(input().rstrip())

answer = sorted(list(dont_hear.intersection(dont_see)))

print(len(answer))
print("\n".join(answer))