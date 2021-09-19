# 문제: [BOJ 21315] 카드 섞기
# 유형: 완전 탐색
# 메모리/시간: 31312kb / 84ms

import sys
from math import log2
from itertools import product

input = sys.stdin.readline


def mix_cards_with_two_kei(cards, n, k):
    # 첫 번째 단계
    cards = cards[-(2 ** k) :] + cards[: n - 2 ** k]
    # 두 번째 단계부터
    for i in range(2, k + 2):
        cards = (
            cards[2 ** (k - i + 2) - 2 ** (k - i + 1) : 2 ** (k - i + 2)]
            + cards[: 2 ** (k - i + 2) - 2 ** (k - i + 1)]
            + cards[2 ** (k - i + 2) :]
        )
    return cards


def guess_two_kei(n, mixed_cards):
    cases = list(product(range(1, int(log2(n)) + 1), repeat=2))  # 가능한 k 조합
    for k1, k2 in cases:
        cards = list(range(1, n + 1))
        cards = mix_cards_with_two_kei(cards, n, k1)  # 첫 번째 (2, k) 섞기
        cards = mix_cards_with_two_kei(cards, n, k2)  # 두 번째 (2, k) 섞기

        # 입력 결과와 같다면
        if cards == mixed_cards:
            return k1, k2


# 입력
n = int(input())  # 카드 수
mixed_cards = list(map(int, input().split()))  # (2, k) 두 번 섞기 결과

# 출력
print(*guess_two_kei(n, mixed_cards))
