###### 3029번: 경고
# https://www.acmicpc.net/problem/3029
# 메모리/시간: 31864KB / 96ms

import sys

input = sys.stdin.readline

now_hour, now_min, now_sec = map(int, input().split(":"))
na_hour, na_min, na_sec = map(int, input().split(":"))

now = now_hour*60*60 + now_min*60 + now_sec
na = na_hour*60*60 + na_min*60 + na_sec

time = (na - now) if (na > now) else (24*60*60 - now + na)

hour = time // (60*60)
time -= hour*60*60
min = time // 60
time -= min*60
sec = time

print(f"{hour:02}:{min:02}:{sec:02}")