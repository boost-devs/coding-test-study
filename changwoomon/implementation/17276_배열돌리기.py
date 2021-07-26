###### 17276번: 배열 돌리기
# https://www.acmicpc.net/problem/17276
# 메모리/시간: 48460KB / 740ms

import sys

input = sys.stdin.readline

T = int(input())

def rotate(n, d, arr):
    if d < 0:
        d += 360
    cnt = d // 45
    for _ in range(cnt):
        mid = n // 2
        for i in range(n):
            arr[i][i], arr[i][mid] = arr[i][mid], arr[i][i]
            arr[i][i], arr[i][n-1-i] = arr[i][n-1-i], arr[i][i]
            arr[i][i], arr[mid][i] = arr[mid][i], arr[i][i]
        for i in range(mid):
            arr[mid][i], arr[mid][n-1-i] = arr[mid][n-1-i], arr[mid][i]
    return arr

for _ in range(T):
    n, d = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]
    for row in rotate(n, d, array):
        print(*row)