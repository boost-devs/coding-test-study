# https://www.acmicpc.net/problem/1806
# 부분합
# 40748 KB / 184 ms


N, S = map(int, input().split())
arr = [int(a) for a in input().split()]

if sum(arr) < S:
    min_length = 0
else:
    start, end = 0, 1
    psum = sum(arr[:1])
    min_length = N
    while start < N and min_length > 1:
        if psum < S:
            if end >= N:
                break
            psum += arr[end]
            end += 1
        else:
            min_length = min(min_length, end - start)
            psum -= arr[start]
            start += 1

print(min_length)
