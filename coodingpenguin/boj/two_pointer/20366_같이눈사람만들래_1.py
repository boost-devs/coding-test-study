# 문제: [BOJ 20366] 같이 눈사람 만들래?
# 유형: 투포인터
# 메모리/시간: 시간초과
# 참고: https://ansohxxn.github.io/boj/20366/

import sys

input = sys.stdin.readline

# 입력
n = int(input())  # 눈덩이 개수
snow = list(map(int, input().split()))  # 눈덩이 지름

min_diff = int(2e9)  # 눈사람 키 차이 최솟값
snow_sum = []  # 가능한 눈사람 높이
for i in range(n):
    for j in range(i + 1, n):
        snow_sum.append((snow[i] + snow[j], i, j))
snow_sum.sort()  # 정렬

for i in range(len(snow_sum)):
    elsa, ey, ex = snow_sum[i]  # 엘사 눈사람
    for j in range(i + 1, len(snow_sum)):
        anna, ay, ax = snow_sum[j]  # 안나 눈사람
        # 선택한 눈이 겹친다면 패스
        if len({ey, ex, ay, ax}) < 4:
            continue
        # 엘사와 안나 눈사람 차이를 구해 최솟값 갱신
        min_diff = min(min_diff, anna - elsa)


# 출력
print(min_diff)
