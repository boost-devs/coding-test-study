###### 1244번: 스위치 켜고 끄기
# https://www.acmicpc.net/problem/1244
# 메모리/시간: 29200KB / 68ms

import sys

input = sys.stdin.readline

N = int(input())

switch = [-1] + list(map(int, input().split()))

def boy(num):
    for i in range(num, N+1, num):
        if switch[i] == 0:
            switch[i] = 1
        else:
            switch[i] = 0

def girl(num):
    for i in range(0, min(N-num, num-1)+1):
        if switch[num-i] == switch[num+i]:
            if switch[num-i] == 0:
                switch[num-i], switch[num+i] = 1, 1
            else:
                switch[num-i], switch[num+i] = 0, 0
        else:
            break

num_student = int(input())

for _ in range(num_student):
    gender, number = map(int, input().split())
    if gender == 1:
        boy(number)
    else:
        girl(number)

for i in range(1, N+1, 20):
    print(*switch[i:i+20])