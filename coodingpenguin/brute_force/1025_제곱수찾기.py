# 문제: [BOJ 1025] 제곱수 찾기
# 유형: 완전 탐색
# 메모리/시간: 29200kb / 144ms
# 참고: https://qgqg264.tistory.com/83

import sys

input = sys.stdin.readline


def is_squared(num_str: str) -> bool:
    num = int(num_str)
    if int(num ** 0.5) ** 2 == num:
        return True
    return False


def get_max_squared(n: int, m: int, table: list) -> int:
    max_squared = -1  # 최대 제곱수
    # 모든 위치에 대해서
    for y in range(n):
        for x in range(m):
            # 모든 등차수열 차수에 대해서
            for dy in range(-n, n):
                for dx in range(-m, m):
                    # 제자리 걸음이면 패스
                    if dy == 0 and dx == 0:
                        continue
                    num = ""  # 만들 수 있는 숫자
                    ny, nx = y, x  # 시작 위치
                    while 0 <= ny < n and 0 <= nx < m:
                        num += table[ny][nx]  # 숫자 갱신
                        # 제곱수라면
                        if is_squared(num):
                            max_squared = max(max_squared, int(num))  # 최댓값과 비교해서 갱신
                        ny, nx = ny + dy, nx + dx  # 다음 위치 갱신
    return max_squared


# 입력
n, m = map(int, input().split())  # 세로, 가로 크기
table = [list(input().rstrip()) for _ in range(n)]  # 표

max_squared = get_max_squared(n, m, table)  # 최대 제곱수

# 출력
if max_squared == -1:
    print(-1)  # 제곱수가 없는 경우
else:
    print(max_squared)
