import sys
input = sys.stdin.readline

input()
arr = []

arr.extend(list(map(int, input().split())))
arr.extend(list(map(int, input().split())))
print(*sorted(arr))