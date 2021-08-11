import sys
from itertools import product
from copy import deepcopy
input = sys.stdin.readline
cases = list(product([0,1],repeat = 8)) # 모든 경우의 수, 경우란 8가지의 경우(행,열,대각선)별로 독립적으로 계산한다.

n= int(input())

for _ in range(n):
    ans = 1000
    arr =[]
    for _ in range(3):
        arr.append([0 if x=='H' else 1 for x in input().split()])
    for case in cases: # 모든 케이스 마다 탐색
        if ans< sum(case):
            continue
        temp_case = deepcopy(arr)
        for i in range(3): # 열별로 탐색
            if case[i] == 1: # 1이면 뒤집음
                ## 뒤집기
                temp_case[i][0] = 1 - temp_case[i][0] 
                temp_case[i][1] = 1 - temp_case[i][1] 
                temp_case[i][2] = 1 - temp_case[i][2] 

        for i in range(3,6): # 행별로 탐색
            if case[i] == 1:
                temp_case[0][i-3] = 1 - temp_case[0][i-3] 
                temp_case[1][i-3] = 1 - temp_case[1][i-3]
                temp_case[2][i-3] = 1 - temp_case[2][i-3]
        if case[6] == 1: # 대각선 1
            temp_case[0][0] = 1 - temp_case[0][0] 
            temp_case[1][1] = 1 - temp_case[1][1]
            temp_case[2][2] = 1 - temp_case[2][2]
        if case[7] == 1: # 대각선 2
            temp_case[2][0] = 1 - temp_case[2][0] 
            temp_case[1][1] = 1 - temp_case[1][1]
            temp_case[0][2] = 1 - temp_case[0][2]
        _sum = sum(map(sum, temp_case)) # 합구하기
        if _sum ==9 or _sum ==0:
            ans = sum(case)
    if ans == 1000:
        print(-1)
    else:
        print(ans)