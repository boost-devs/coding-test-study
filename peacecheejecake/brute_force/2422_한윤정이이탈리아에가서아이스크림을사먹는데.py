# https://www.acmicpc.net/problem/2422
# 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
# 29468 KB / 112 ms


import sys

input = sys.stdin.readline


N, M = map(int, input().split())
checker = {
    i:set(range(i + 1, N + 1)) for i in range(1, N + 1)
}
for _ in range(M):
    i, j = sorted(map(int, input().split()))
    checker[i].remove(j)

num_cases = 0
for i in range(1, N + 1):
    for j in checker[i]:
        num_cases += len(checker[j] & checker[i])

print(num_cases)
