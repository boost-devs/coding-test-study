###### 2422번: 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
# https://www.acmicpc.net/problem/2422
# 메모리/시간: 29200KB / 536ms

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

do_not = [[False] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    do_not[a][b] = True
    do_not[b][a] = True

cnt = 0

for i in range(1, N+1):
    for j in range(i+1, N+1):
        if do_not[i][j]:
            continue
        for k in range(j+1, N+1):
            if any([do_not[i][k], do_not[j][k]]):
                continue
            cnt += 1

print(cnt)