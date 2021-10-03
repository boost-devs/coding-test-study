# 문제: [BOJ 20366] 같이 눈사람 만들래?
# 유형: 투포인터
# 메모리/시간: 125588kb / 484ms (PyPy3)
# 참고: https://ansohxxn.github.io/boj/20366/

import sys

input = sys.stdin.readline

# 입력
n = int(input())  # 눈덩이 개수
snow = sorted(map(int, input().split()))  # 눈덩이 지름

min_diff = int(2e9)  # 눈사람 키 차이 최솟값
for i in range(n - 3):
    for j in range(i + 3, n):
        elsa = snow[i] + snow[j]  # 엘사 눈사람 높이
        left, right = i + 1, j - 1  # 왼쪽/오른쪽 포인터
        while left < right:
            anna = snow[left] + snow[right]  # 안나 눈사람 높이
            diff = anna - elsa  # 높이차
            min_diff = min(min_diff, abs(diff))  # 최솟값 갱신
            # 높이차가 양수라면
            if diff > 0:
                # 높이차를 0에 수렴하도록
                # 오른쪽 포인터를 이동
                right -= 1
            # 높이차가 음수라면
            else:
                # 높이차가 0에 수렴하도록
                # 왼쪽 포인터를 이동
                left += 1

# 출력
print(min_diff)  # 눈사람 키 차이 최솟값
