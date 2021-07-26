# https://www.acmicpc.net/problem/1912
# 연속합
# 37164 KB / 128 ms


n = int(input())
numbers = [int(x) for x in input().split()]
for i in range(1, n):
    numbers[i] += max(0, numbers[i - 1])

print(max(numbers))
