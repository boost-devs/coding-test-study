import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[0]*(n+1)]
for i in range(n):
    _input = list(map(int, input().split()))
    arr.append([0] + _input)

for i in range(1, n+1):
    for j in range(1, n+1):
        arr[i][j] += arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(arr[x2][y2]-arr[x2][y1-1]-arr[x1-1][y2]+arr[x1-1][y1-1])