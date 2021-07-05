# 문제: [BOJ 15486] 퇴사 2
# 유형: 동적계획법
# 메모리/시간: 166244kb / 2704ms
# 참고: https://dndi117.tistory.com/entry/aaa

import sys

input = sys.stdin.readline


def result(n, times, pays):
    table = [0] * (n + 2)
    max_pay = 0  # 최대 이익
    for i in range(n + 2):
        max_pay = max(max_pay, table[i])
        # 퇴사 후 상담이 있다면
        if i + times[i] > n + 1:
            continue
        # 없다면 상담이 끝난 후의 이익 갱신
        table[i + times[i]] = max(table[i + times[i]], max_pay + pays[i])
    return max_pay


n = int(input())  # 최대 일수
times, pays = [0] * (n + 2), [0] * (n + 2)  # 급여, 상담일수
for i in range(1, n + 1):
    t, p = map(int, input().split())
    times[i], pays[i] = t, p

print(result(n, times, pays))
