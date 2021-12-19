###### 3151번: 합이 0
# https://www.acmicpc.net/problem/3151
# 메모리/시간: 125680KB / 556ms (PyPy3)

import sys

input = sys.stdin.readline

N = int(input())

A = sorted(list(map(int, input().split())))

cnt = 0

for i in range(N-2):
    left, right = i+1, N-1
    target = A[i]
    while (left < right):
        _sum = A[left] + A[right]
        if _sum + target == 0:
            cond = False
            if A[left] == A[right]:
                cnt += right - left
            else:
                j = left + 1
                k = right - 1
                while (A[left] == A[j]) and (j < right):
                    j += 1
                    cond = True
                while (A[right] == A[k]) and (left < k):
                    k -= 1
                cnt += (j - left) * (right - k)
            if cond:
                left = j
            else:
                left += 1
        elif _sum + target > 0:
            right -=1
        else:
            left += 1

print(cnt)