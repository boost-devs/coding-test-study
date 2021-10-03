# 문제: [BOJ 20437] 문자열 게임2
# 유형: 딕셔너리
# 메모리/시간: 32156kb / 240ms

import sys
from collections import defaultdict

input = sys.stdin.readline


def do_game():
    loc = defaultdict(list)  # 문자의 위치 저장
    count = defaultdict(int)  # 문자의 개수 저장

    for idx, letter in enumerate(W):
        loc[letter].append(idx)
        count[letter] += 1

    for k, v in count.items():
        # 정수 K보다 작으면 제외
        if v < K:
            del loc[k]

    # 남은 문자가 없다면
    if not loc:
        return -1, -1

    diff = []  # 위치 간 거리 계산
    for k, l in loc.items():
        for i in range(len(l) - K + 1):
            diff.append(l[i + K - 1] - l[i] + 1)

    # 최소 길이와 최대 길이 반환
    return min(diff), max(diff)


T = int(input())  # 테스트 케이스 개수
for _ in range(T):
    W, K = input().rstrip(), int(input())  # 문자열, 정수
    # 정수가 1이라면
    if K == 1:
        # 연속 문자열 길이 모두 1
        print(1, 1)
    # 정수가 1이 아니라면
    else:
        l1, l2 = do_game()
        # 연속 문자열이 없는 경우
        if l1 == -1:
            print(-1)
        # 연속 문자열이 있는 경우
        else:
            print(l1, l2)
