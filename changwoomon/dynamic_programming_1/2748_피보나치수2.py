###### 2748번: 피보나치 수 2
# https://www.acmicpc.net/problem/2748
# 메모리/시간: 29200KB / 68ms

import sys

input = sys.stdin.readline

n = int(input())

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

print(fibonacci(n))