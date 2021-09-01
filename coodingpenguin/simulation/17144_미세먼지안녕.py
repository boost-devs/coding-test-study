import sys
from copy import deepcopy

input = sys.stdin.readline
clockwise = [(0, 1), (1, 0), (0, -1), (-1, 0)]
counter_clockwise = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def get_air_purifier_loc(r, c, arr):
    for y in range(r):
        if arr[y][0] == -1:
            return [y, y + 1]


def spread_dirt(r, c, arr):
    new_arr = deepcopy(arr)
    for y in range(r):
        for x in range(c):
            if arr[y][x] in (-1, 0):
                continue
            sub_dirt = arr[y][x] // 5
            for dy, dx in clockwise:
                ny, nx = y + dy, x + dx
                if (ny >= r or ny < 0) or (nx >= c or nx < 0):
                    continue
                new_arr[ny][nx] += sub_dirt
                new_arr[y][x] -= sub_dirt
    return new_arr


def activate_air_purifier(r, c, arr, loc):
    new_arr = deepcopy(arr)
    top_y, top_x = loc[0], 1
    bot_y, bot_x = loc[1], 1
    pointer = 0
    while True:
        top_dirt = arr[top_y][top_x]
        new_arr[top_y][top_x] = 0
        top_y, top_x = (
            top_y + counter_clockwise[pointer][0],
            top_x + counter_clockwise[pointer][1],
        )
        if (top_y >= r or top_y < 0) or (top_x >= c or top_x < 0):
            top_y, top_x = (
                top_y - counter_clockwise[pointer][0],
                top_x - counter_clockwise[pointer][1],
            )
            pointer += 1
            top_y, top_x = (
                top_y + counter_clockwise[pointer][0],
                top_x + counter_clockwise[pointer][1],
            )
        if arr[top_y][top_x] == -1:
            break
        new_arr[top_y][top_x] = top_dirt
        print(f"({top_y}, {top_x})")
        for row in new_arr:
            print(*row)
        print("=" * 30)
    pointer = 0
    while True:
        bot_dirt = arr[bot_y][bot_x]
        bot_y, bot_x = bot_y + clockwise[pointer][0], bot_x + clockwise[pointer][1]
        if (bot_y >= r or bot_y < 0) or (bot_x >= c or bot_x < 0):
            bot_y, bot_x = bot_y - clockwise[pointer][0], bot_x - clockwise[pointer][1]
            pointer += 1
            bot_y, bot_x = bot_y + clockwise[pointer][0], bot_x + clockwise[pointer][1]
        if arr[bot_y][bot_x] == -1:
            break
        new_arr[bot_y][bot_x] = bot_dirt
        for row in new_arr:
            print(*row)
        print("=" * 30)
    return new_arr


def calculate_total_dirt(r, c, arr):
    total_dirt = 0
    for y in range(r):
        for x in range(c):
            if arr[y][x] in (-1, 0):
                continue
            total_dirt += arr[y][x]
    return total_dirt


def get_total_dirt(r, c, t, arr):
    loc = get_air_purifier_loc(r, c, arr)
    for _ in range(t):
        arr = spread_dirt(r, c, arr)
        arr = activate_air_purifier(r, c, arr, loc)
    for row in arr:
        print(*row)
    return calculate_total_dirt(r, c, arr)


r, c, t = map(int, input().split())  # 격자판 세로, 가로, 시간
arr = [list(map(int, input().split())) for _ in range(r)]  # 격자판 정보
print("=" * 30)
print(get_total_dirt(r, c, t, arr))
