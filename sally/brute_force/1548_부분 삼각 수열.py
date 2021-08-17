# Brute Force
# Problem: 1548
# Memory: 29200KB
# Time: 72ms

N = int(input())
arr = list(map(int, input().split()))

if N > 2:
    result = 2
    arr.sort()
    for i in range(len(arr)-2):
        target = arr[i] + arr[i+1]
        ret = N - i
        for j in range(i+2, N):
            if target <= arr[j]:
                ret = j - i
                break
        result = max(result, ret)
else: result = N

print(result)