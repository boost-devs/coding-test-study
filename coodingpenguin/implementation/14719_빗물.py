import sys

input = sys.stdin.readline


def get_total_water(walls):
    if len(walls) == 1:
        return 0
    total_water = 0
    for i in range(1, len(walls) - 1):
        left = max(walls[:i])
        right = max(walls[i + 1 :])
        standard = min(left, right)
        if standard >= walls[i]:
            total_water += standard - walls[i]
    return total_water


h, w = map(int, input().split())
walls = list(map(int, input().split()))

print(get_total_water(walls))
