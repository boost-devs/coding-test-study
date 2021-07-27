# 문제: [BOJ 20164] 홀수 홀릭 호석
# 유형: 구현, 재귀
# 메모리/시간: 29200kb / 80ms
# 참고: https://boomrabbit.tistory.com/93

import sys

input = sys.stdin.readline


def get_odds(num):
    count = 0  # 홀수 개수
    for i in num:
        if int(i) % 2:
            count += 1
    return count


def dfs(num, count):
    global min_count, max_count
    # 길이가 1이라면
    if len(num) == 1:
        count += get_odds(num)
        # 최솟값과 최댓값 갱신
        min_count = min(min_count, count)
        max_count = max(max_count, count)
        return
    # 길이가 2라면
    elif len(num) == 2:
        count += get_odds(num)
        new_num = int(num[0]) + int(num[1])  # 새로운 숫자 조합
        dfs(str(new_num), count)
    else:
        count += get_odds(num)
        length = len(num)
        # 모든 경우의 수에 대해
        for i in range(1, length):
            for j in range(i + 1, length):
                new_num = int(num[:i]) + int(num[i:j]) + int(num[j:])  # 새로운 숫자 조합
                dfs(str(new_num), count)


num = input().rstrip()  # 처음 가진 수
min_count, max_count = int(1e9), -1  # 홀수개수 최솟값, 최댓값
dfs(str(num), 0)
print(min_count, max_count)
