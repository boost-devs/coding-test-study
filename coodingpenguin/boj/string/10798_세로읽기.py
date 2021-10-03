# 문제: [BOJ 10798] 세로 읽기
# 유형: 문자열
# 메모리/시간: 29200kb / 68ms

import sys

input = sys.stdin.readline


def add_padding():
    max_len = max(map(len, lines))  # 문자열의 최대 길이
    for line in lines:
        l = len(line)
        line.extend([""] * (max_len - l))  # 남은 공간만큼 패딩 추가


# 입력
lines = [list(input().rstrip()) for _ in range(5)]

# 최대 길이 보다 작다면 패딩 추가
add_padding()

result = ""  # 결과 문자열
for vert_line in zip(*lines):
    result += "".join(vert_line)

# 출력
print(result)
