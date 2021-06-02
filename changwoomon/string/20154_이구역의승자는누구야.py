###### 20154번: 이 구역의 승자는 누구야?!
# https://www.acmicpc.net/problem/20154
# 메모리/시간: 49600KB / 552ms

import sys
from collections import deque

input = sys.stdin.readline

alphabet = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3, 'G': 3, 'H': 3, 'I': 1, 'J': 1, 'K': 3, 'L': 1, 'M': 3, 'N': 3, 'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 2, 'X': 2, 'Y': 2, 'Z': 1}

_input = [alphabet[x] for x in list(map(str, input().rstrip()))]
queue = deque(_input)

while len(queue) > 1:
    _tmp = deque()
    for _ in range(len(queue) // 2):
        a = queue.popleft()
        b = queue.popleft()
        _tmp.append((a + b) % 10)
    if len(queue) % 2 != 0:
        _tmp.append(queue.popleft())
    queue = _tmp

print("I'm a winner!") if queue.popleft() % 2 == 1 else print("You're the winner?")