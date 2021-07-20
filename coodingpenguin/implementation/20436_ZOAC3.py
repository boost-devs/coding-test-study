# 문제: [BOJ 20436] ZOAC 3
# 유형: 구현
# 메모리/시간: 29200kb / 68ms

import sys

input = sys.stdin.readline

left = {  # 한글 자음 자판 영문키와 위치
    "q": (0, 0),
    "w": (0, 1),
    "e": (0, 2),
    "r": (0, 3),
    "t": (0, 4),
    "a": (1, 0),
    "s": (1, 1),
    "d": (1, 2),
    "f": (1, 3),
    "g": (1, 4),
    "z": (2, 0),
    "x": (2, 1),
    "c": (2, 2),
    "v": (2, 3),
}

right = {  # 한글 모음 자판 영문키와 위치
    "y": (0, 5),
    "u": (0, 6),
    "i": (0, 7),
    "o": (0, 8),
    "p": (0, 9),
    "h": (1, 5),
    "j": (1, 6),
    "k": (1, 7),
    "l": (1, 8),
    "b": (2, 4),
    "n": (2, 5),
    "m": (2, 6),
}


def calculate_time(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1]) + 1


sl, sr = input().rstrip().split()  # 왼손, 오른손 손가락 위치 키
word = input().rstrip()  # 입력할 문자
time = 0  # 걸리는 시간

for letter in word:
    # 문자 위치로 존재하지 않으면 None 반환
    posl = left.get(letter, None)
    posr = right.get(letter, None)
    # 왼쪽 자판을 누른다면
    if posl:
        time += calculate_time(left[sl], posl)  # 걸리는 시간 계산
        sl = letter  # 왼손 위치 갱신
    # 오른쪽 자판을 누른다면
    if posr:
        time += calculate_time(right[sr], posr)  # 걸리는 시간 계산
        sr = letter  # 오른손 위치 갱신

print(time)
