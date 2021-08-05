# 문제: [BOJ 2503] 숫자 야구
# 유형: 완전 탐색
# 메모리/시간: 29200kb / 76ms

import sys

input = sys.stdin.readline


def remove_candidates(num: str, strike: int, ball: int) -> None:
    cands = answers.copy()
    for cand in cands:
        cand_strike = len([a for a, b in zip(num, cand) if a == b])  # 후보의 스트라이크 수
        cand_ball = len(set(num) & set(cand)) - cand_strike  # 후보의 볼 수
        # 볼이나 스크라이크가 일치하지 않으면
        if strike != cand_strike or ball != cand_ball:
            answers.remove(cand)  # 후보에서 제외


# 입력
n = int(input())  # 질문 수

answers = []  # 가능한 정답 후보
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or k == i:
                continue
            answers.append(str(i) + str(j) + str(k))

for _ in range(n):
    num, strike, ball = map(int, input().split())
    remove_candidates(str(num), strike, ball)  # 맞지 않는 후보 제거

# 출력
print(len(answers))
