import sys
from collections import defaultdict

input = sys.stdin.readline


def result(n, k, arr):
    counter = defaultdict(int)
    start, end = 0, 0
    max_length = -1
    while end < n:
        if counter.get(arr[end], 0) < k:
            counter[arr[end]] += 1
            end += 1
        else:
            max_length = max(max_length, end - start)
            counter[arr[start]] -= 1
            start += 1

    return max(max_length, end - start)


N, K = map(int, input().split())
arr = list(map(int, input().split()))

print(result(N, K, arr))
