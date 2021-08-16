import sys
from itertools import product
input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

cases = list(product([0,1],repeat=n))
_min = 1000000
for case in cases[:(2**n)+1]:  # 절반까지만 보면됨
    team1 = []
    team2 = []
    for i in range(n): # 비트마스크에 따른 팀 분배
        if case[i]:
            team2.append(i)
        else:
            team1.append(i)
    _team1 = 0
    # 팀 점수 구하기
    for member in team1:
        for synergy in team1:
            if member != synergy:
                _team1 += arr[member][synergy]
    _team2 = 0
    for member in team2:
        for synergy in team2:
            if member != synergy:
                _team2 += arr[member][synergy]
    _min = min(_min,abs(_team2-_team1))
print(_min)