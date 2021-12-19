###### 1010번: 다리 놓기
# https://www.acmicpc.net/problem/1010
# 메모리/시간: 29200KB / 72ms

import sys

input = sys.stdin.readline

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    print(int(factorial(M) / (factorial(N) * factorial(M-N))))