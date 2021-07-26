# https://www.acmicpc.net/problem/11053
# 가장 긴 증가하는 부분 수열
# 29200 KB / 204 ms

n = int(input())
arr = [int(x) for x in input().split()]
table = [1] * n
for i, a in enumerate(arr):
    for j in range(i):
        if arr[i] > arr[j]:
            table[i] = max(table[i], table[j] + 1)
print(max(table))
