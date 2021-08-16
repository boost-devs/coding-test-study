# 문제: [BOJ 15661] 링크와 스타트
# 유형: 완전 탐색
# 메모리/시간: 156744b / 2244ms (PyPy3)

import sys

input = sys.stdin.readline


def add_ability(members: list, new_member: int, ability: int) -> int:
    for member in members:
        ability += table[member][new_member]
        ability += table[new_member][member]
    return ability


def remove_ability(members: list, removed_member: int, ability: int) -> int:
    for member in members:
        ability -= table[member][removed_member]
        ability -= table[removed_member][member]
    return ability


def calculate_diff(members: list, ability: int) -> int:
    others = []
    others_ability = 0
    for i in range(n):
        if i not in members:
            if others:
                others_ability = add_ability(others, i, others_ability)
            others.append(i)
    return abs(others_ability - ability)


def dfs(members: list, ability: int):
    global min_diff
    min_diff = min(min_diff, calculate_diff(members, ability))  # 능력치 차이 갱신
    # 마지막 멤버라면
    if members[-1] == n - 1:
        return  # 종료
    # 가능한 모든 선수에 대해서
    for i in range(members[-1] + 1, n):
        # 새로운 선수 투입
        ability = add_ability(members, i, ability)
        members.append(i)
        dfs(members, ability)  # 계속 조합
        # 새로운 선수 빼기
        members.pop()
        ability = remove_ability(members, i, ability)


# 입력
n = int(input())  # 사람 수
table = [list(map(int, input().split())) for _ in range(n)]  # 능력치 조합 테이블

min_diff = int(1e9)  # 능력 최소 차
for i in range(n // 2 + 1):
    dfs([i], 0)  # 팀 조합

# 출력
print(min_diff)
