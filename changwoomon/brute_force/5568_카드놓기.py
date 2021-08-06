###### 5568번: 카드 놓기
# https://www.acmicpc.net/problem/5568
# 메모리/시간: KB / ms

import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())

k = int(input())

card = [int(input()) for _ in range(n)]

print(len(set("".join(str(x).replace('(', '').replace(',', '').replace(' ', '').replace(')', '')) for x in permutations(card, k))))