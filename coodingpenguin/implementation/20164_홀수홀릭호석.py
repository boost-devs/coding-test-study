import sys
from itertools import combinations

input = sys.stdin.readline


def get_odds(num):
    count = 0
    for i in num:
        if int(i) % 2:
            count += 1
    return count


def dfs(num, count):
    global min_count, max_count
    result = 0
    if len(num) == 1:
        count += get_odds(num)
        min_count = min(min_count, count)
        max_count = max(max_count, count)
        return
    elif len(num) == 2:
        count += get_odds(num)
        new_num = int(num[0]) + int(num[1])
        dfs(str(new_num), count)
    else:
        count += get_odds(num)
        length = len(num)
        for i in range(1, length):
            for j in range(i + 1, length):
                new_num = int(num[:i]) + int(num[i:j]) + int(num[j:])
                dfs(str(new_num), count)


num = input().rstrip()  # 처음 가진 수
min_count, max_count = int(1e9), -1
dfs(str(num), 0)
print(min_count, max_count)
