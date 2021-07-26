# 문제: [BOJ 1244] 스위치 켜고 끄기
# 유형: 구현
# 메모리/시간: 29200kb / 68ms

import sys

input = sys.stdin.readline


def change_status(pos):
    switches[pos] = 1 - switches[pos]


n = int(input())  # 스위치 개수
switches = [-1] + list(map(int, input().split()))  # 스위치 상태
m = int(input())  # 학생 수
acts = [list(map(int, input().split())) for _ in range(m)]  # 학생 순서

for gen, num in acts:
    # 남학생인 경우
    if gen == 1:
        # num의 배수 상태 위치 바꾸기
        for i in range(num, n + 1, num):
            change_status(i)
    # 여학생인 경우
    else:
        change_status(num)  # 현재 위치 바꾸고
        k = min(n - num, num - 1)
        for i in range(1, k + 1):
            # 대칭하는 경우 모두 바꾼다
            if switches[num - i] == switches[num + i]:
                change_status(num - i)
                change_status(num + i)
            else:
                break

# 스위치 상태 20씩 끊어서 출력
switches = switches[1:]
for i in range(0, n, 20):
    print(*switches[i : i + 20])
