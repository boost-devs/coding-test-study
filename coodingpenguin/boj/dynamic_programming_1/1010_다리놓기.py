# 문제: [BOJ 29200] 다리 놓기
# 유형: 동적계획법
# 메모리/시간: 29200kb / 64ms

import sys

input = sys.stdin.readline

table = [[0] * 31 for _ in range(31)]  # 테이블
for i in range(1, 31):
    for j in range(1, 31):
        if i == 1 or j == 1:
            table[i][j] = i * j
        elif i == j:
            table[i][j] = 1
        elif i < j:
            table[i][j] = sum(table[i - 1][i - 1 : j])
        else:
            table[i][j] = table[j][i]


t = int(input())  # 테스트 케이스 개수
for _ in range(t):
    n, m = map(int, input().split())  # 서쪽, 동쪽 사이트 수
    print(table[n][m])  # 다리를 지을 수 있는 경우의 수
