# 문제: [BOJ 15686] 치킨 배달
# 유형: 완전 탐색, 조합
# 메모리/시간: 29452kb / 496ms
# 참고: https://somjang.tistory.com/entry/BaekJoon-15686번-치킨-배달-Python

import sys
from itertools import combinations

input = sys.stdin.readline


def get_chicken_and_home_pos(n, arr):
    chicken, home = [], []
    for y in range(n):
        for x in range(n):
            # 가정집인 경우
            if arr[y][x] == 1:
                home.append((y, x))
            # 치킨집인 경우
            if arr[y][x] == 2:
                chicken.append((y, x))
    return chicken, home


def get_smallest_dist(n, m, arr):
    chicken_pos, home_pos = get_chicken_and_home_pos(n, arr)  # 치킨집, 가정집 위치 리스트
    combs = list(combinations(chicken_pos, m))  # 크기 m에 가능한 조합들
    min_chicken_dist_sum = int(1e9)  # 최소 치킨거리 총합
    # 모든 조합에 대하여
    for comb in combs:
        chicken_dist_sum = 0  # 치킨 거리 합
        # 각 집에 대해서
        for hy, hx in home_pos:
            chicken_dist = 100  # 최소 치킨 거리
            # 가능한 치킨집에서의 최소 치킨 거리를 구한다
            for cy, cx in comb:
                chicken_dist = min(chicken_dist, abs(hy - cy) + abs(hx - cx))
            chicken_dist_sum += chicken_dist  # 합에 추가
        # 최소 치킨거리 총합과 비교하여 최솟값으로 갱신
        min_chicken_dist_sum = min(min_chicken_dist_sum, chicken_dist_sum)
    return min_chicken_dist_sum


# 입력
n, m = map(int, input().split())  # 도시 크기, 유지 가게수
arr = [list(map(int, input().split())) for _ in range(n)]  # 도시정보

# 출력
print(get_smallest_dist(n, m, arr))  # 최소 치킨거리 총합
