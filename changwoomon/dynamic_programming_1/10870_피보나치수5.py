###### 10870번: 피보나치 수 5
# https://www.acmicpc.net/problem/10870
# 메모리/시간: 29200KB / 68ms

import sys

input = sys.stdin.readline

n = int(input())

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(n))