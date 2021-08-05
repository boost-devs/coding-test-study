###### 20366번: 같이 눈사람 만들래?
# https://www.acmicpc.net/problem/20366
# 메모리/시간: 125656KB / 512ms (PyPy3)

import sys

input = sys.stdin.readline

N = int(input())

H = sorted(list(map(int, input().split())))

min_diff = 2 * 10**9

for i in range(N):
    for j in range(N-1, i, -1):
        elsa = H[i] + H[j]
        left, right = i+1, j-1
        while (left < right):
            anna = H[left] + H[right]
            diff = elsa - anna
            min_diff = min(min_diff, abs(diff))
            if diff > 0:
                left += 1
            else:
                right -= 1

print(min_diff)