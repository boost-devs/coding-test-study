# 문제: [BOJ 3029] 경고
# 유형: 문자열
# 메모리/시간: 29200kb / 68ms

import sys

input = sys.stdin.readline


def parse_string(string):
    hour, minute, second = map(int, string.split(":"))
    return second, minute, hour


def diff_time(current_time, throw_time):
    # second
    second = throw_time[0] - current_time[0]
    second_carry = False
    if second < 0:
        second += 60
        second_carry = True

    # minute
    throw_minute = throw_time[1] - 1 if second_carry else throw_time[1]
    minute = throw_minute - current_time[1]
    minute_carry = False
    if minute < 0:
        minute += 60
        minute_carry = True

    # hour
    throw_hour = throw_time[2] - 1 if minute_carry else throw_time[2]
    hour = throw_hour - current_time[2]
    if hour < 0:
        hour += 24

    return hour, minute, second


def format_time(wait_time):
    hour, minute, second = wait_time
    return f"{hour:02}:{minute:02}:{second:02}"


# 입력
current_time = parse_string(input().rstrip())  # 현재 시간
throw_time = parse_string(input().rstrip())  # 던진 시간

# 시분초가 동일하다면
if current_time == throw_time:
    # 24시간 기다린 것
    wait_time = (24, 0, 0)
# 아닐 경우
else:
    # 차이를 계산
    wait_time = diff_time(current_time, throw_time)  # 기다린 시간

# 출력
print(format_time(wait_time))
