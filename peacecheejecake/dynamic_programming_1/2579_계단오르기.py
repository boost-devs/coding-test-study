# https://www.acmicpc.net/problem/2579
# 계단 오르기
# 29200 KB / 64 ms

import sys


def input():
    return sys.stdin.readline().strip()


num_steps = int(input())
steps = []
for _ in range(num_steps):
    steps.append(int(input()))

if num_steps < 3:
    max_score = sum(steps)
else:
    best_scores = [
        steps[0], # 1층: 무조건 밟을 때 최대
        sum(steps[:2]), # 2층: 전부 밟을 때 최대
        max(steps[:2]) + steps[2], # 3층: 1, 2층 중 더 큰 점수를 밟을 때 최대
    ]
    for i in range(3, num_steps):
        best_score = max(
            best_scores[i - 2], # i - 1번째 계단 밟지 않았을 때
            best_scores[i - 3] + steps[i - 1], # i - 1번째 계단 밟았을 때
        ) + steps[i]
        best_scores.append(best_score)
    max_score = best_scores[-1]

print(max_score)
