# 문제: [BOJ 9655] 돌 게임
# 유형: 수학
# 메모리/시간: 29200kb / 72ms

import sys

input = sys.stdin.readline

n = int(input())
games = ["CY", "SK"]
print(games[n % 2])
