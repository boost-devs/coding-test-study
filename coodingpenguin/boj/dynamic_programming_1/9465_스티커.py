# 문제: [BOJ 9265] 스티커
# 유형: 동적계획법
# 메모리/시간: 63584kb / 1432ms

import sys

input = sys.stdin.readline


def find_max_score(n, arr):
    table = [{"top": arr[0][0], "bot": arr[1][0], "not": 0}]  # 테이블
    # 한 컬럼씩 순회하며
    for i in range(1, n):
        current = {
            "top": max(table[i - 1]["bot"], table[i - 1]["not"])
            + arr[0][i],  # 위쪽 스티커 선택
            "bot": max(table[i - 1]["top"], table[i - 1]["not"])
            + arr[1][i],  # 아래쪽 스티커 선택
            "not": max(table[i - 1].values()),  # 어떤 스티커도 선택하지 않음
        }
        table.append(current)
    max_score = max([max(i.values()) for i in table])  # 테이블 중 최대값
    return max_score


t = int(input())  # 테스트 케이스 개수
for _ in range(t):
    n = int(input())  # 스티커 컬럼 수
    arr = [list(map(int, input().split())) for _ in range(2)]  # 스터커 점수
    print(find_max_score(n, arr))
