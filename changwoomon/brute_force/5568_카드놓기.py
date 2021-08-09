###### 5568번: 카드 놓기
# https://www.acmicpc.net/problem/5568
# 메모리/시간: 29452KB / 72ms

import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())

k = int(input())

card = [int(input()) for _ in range(n)]

print(len(set("".join(map(str, x)) for x in permutations(card, k))))