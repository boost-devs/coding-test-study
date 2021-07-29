import sys
from collections import deque

input = sys.stdin.readline


def get_max_visitors(size, visitors):
    if size == 1:
        return max(visitors), 1
    if not sum(visitors):
        return None, "SAD"
    window = sum(visitors[:size])
    max_visitors = window
    count = 1

    for i in range(size, len(visitors)):
        window += visitors[i]
        window -= visitors[i - size]
        if window > max_visitors:
            max_visitors = window
            count = 1
        elif window == max_visitors:
            count += 1

    return max_visitors, count


N, X = map(int, input().split())  # 지난 일수, 기간
visitors = list(map(int, input().split()))
max_visitors, count = get_max_visitors(X, visitors)
if not max_visitors:
    print(count)
else:
    print(max_visitors)
    print(count)
