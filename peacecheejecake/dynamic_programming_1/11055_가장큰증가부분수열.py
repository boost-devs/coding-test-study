# https://www.acmicpc.net/problem/11055
# 가장 큰 증가 부분 수열
# 29200 KB / 176 ms


N = int(input())
arr = [int(x) for x in input().split()]

table = []
for i, a in enumerate(arr):
    if i == 0:
        table.append(a)
    else:
        max_sum = 0
        for j in range(i):
            if arr[j] < arr[i]:
                max_sum = max(max_sum, table[j])
        table.append(max_sum + arr[i])

print(max(table))
