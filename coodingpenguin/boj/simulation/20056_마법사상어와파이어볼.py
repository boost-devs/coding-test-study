# 문제: [BOJ 20056] 마법사 상어와 파이어볼
# 유형: 시뮬레이션, 구현
# 메모리/시간: 34084kb / 488ms, 161936kb / 400ms (PyPy3)

import sys
from collections import defaultdict

input = sys.stdin.readline
dirs = [
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
]  # ↑, ↗, →, ↘, ↓, ↙, ←,


def move_fireball(n, loc):
    new_loc = defaultdict(list)  # 새로운 위치별 파이어볼의 정보
    for r, c in loc:
        for m, s, d in loc[(r, c)]:
            nr, nc = (r + s * dirs[d][0]) % n, (c + s * dirs[d][1]) % n
            new_loc[(nr, nc)].append((m, s, d))
    return new_loc


def check_all_same(fires):
    sum_dirs = sum([d % 2 for _, __, d in fires])  # 0이면 짝, 1이면 홀
    # 모두 짝이거나 모두 홀인 경우
    if sum_dirs in (0, len(fires)):
        return True
    return False


def split_fireball(loc):
    new_loc = defaultdict(list)  # 새로운 위치별 파이어볼의 정보
    for (
        r,
        c,
    ) in loc:
        num_of_fires = len(loc[(r, c)])  # 현재 위치의 파이어볼 개수
        # 개수가 0이라면
        if num_of_fires == 0:
            continue  # 패스한다
        # 개수가 1이라면
        elif num_of_fires == 1:
            new_loc[(r, c)] = loc[(r, c)]  # 파이어볼을 그대로 가져온다
        # 개수가 2이상이라면
        else:
            nm = sum([m for m, _, __ in loc[(r, c)]]) // 5  # 새로운 질량
            ns = sum([s for _, s, __ in loc[(r, c)]]) // num_of_fires  # 새로운 속력
            # 질량이 0이라면
            if nm == 0:
                continue  # 소멸시킨다
            # 방향이 모두 홀이거나 짝이라면
            if check_all_same(loc[(r, c)]):
                # 0, 2, 4, 6으로 가는 파이어볼을 생성한다
                new_loc[(r, c)] = [(nm, ns, d) for d in (0, 2, 4, 6)]
            # 아니라면
            else:
                # 1, 3, 5, 7으로 가는 파이어볼을 생성한다
                new_loc[(r, c)] = [(nm, ns, d) for d in (1, 3, 5, 7)]
    return new_loc


def calculate_total_mass(loc):
    total_mass = 0  # 총 질량
    for r, c in loc:
        for m, _, __ in loc[(r, c)]:
            total_mass += m
    return total_mass


def magic_fireball(n, k, info):
    loc = defaultdict(list)  # 위치별 파이어볼의 정보
    for _r, _c, _m, _s, _d in info:
        loc[(_r - 1, _c - 1)].append((_m, _s, _d))
    # 다음의 과정을 k번 수행한다
    for _ in range(k):
        loc = move_fireball(n, loc)  # 파이어볼을 이동한다
        loc = split_fireball(loc)  # 2개 이상의 파이어볼을 분리시킨다
    # 남아 있는 파이어볼 질량의 합을 구한다
    return calculate_total_mass(loc)


n, m, k = map(int, input().split())  # 격자판 크기, 파이어볼 개수, 명령 횟수
info = [list(map(int, input().split())) for _ in range(m)]  # 파이어볼 정보

print(magic_fireball(n, k, info))  # 파이어볼 질량의 합
