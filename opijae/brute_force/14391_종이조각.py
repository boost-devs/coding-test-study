import sys
from itertools import product
input = sys.stdin.readline
n,m = map(int, input().split())
arr=[]

for _ in range(n):
    arr.append([int(x) for x in input().strip()]) # 모든 칸마다 가로로 거할지 세로로 더할지 판단하는 비트마스크
cases = product([0,1],repeat=n*m)
_max = 0
for case in cases:
    _sum = 0
    # 가로로로 더하는 경우 체크
    for i in range(n):
        _temp = 0
        for j in range(m):
            index = i *m +j
            if case[index]:
                # 이전꺼에 * 10
                _temp = _temp*10 + arr[i][j]
            else:
                _sum += _temp
                _temp = 0
        _sum += _temp

    # 세로로로 더하는 경우 체크
    for j in range(m):
        _temp = 0
        for i in range(n):
            index = i *m +j
            if not case[index]:
                _temp = _temp*10 + arr[i][j]
            else:
                _sum += _temp
                _temp = 0
        _sum += _temp

    _max = max(_max,_sum)
print(_max)
