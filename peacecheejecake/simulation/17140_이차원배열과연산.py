# https://www.acmicpc.net/problem/17140
# 31780 KB / 156 ms


from collections import Counter


r, c, k = map(int, input().split())
r, c = r - 1, c - 1
arr = [[0] * 100 for _ in range(100)]
for i in range(3):
    for j, x in enumerate(input().split()):
        arr[i][j] = int(x)

max_row, max_col = 3, 3
for t in range(100):
    if arr[r][c] == k:
        break

    if max_row >= max_col:
        _max_col = max_col
        max_col = 0
        for i in range(max_row):
            counter = sorted(
                Counter(x for x in arr[i] if x > 0).most_common(), 
                key=lambda p: (p[1], p[0]),
            )
            if not counter:
                break

            for j, (num, cnt) in enumerate(counter):
                if j >= 50:
                    break
                arr[i][2 * j] = num
                arr[i][2 * j + 1] = cnt
            else:
                for jj in range(2 * (j + 1), _max_col):
                    arr[i][jj] = 0

            max_col = max(max_col, 2 * (j + 1))
    else:
        _max_row = max_row
        max_row = 0
        for j in range(max_col):
            counter = sorted(
                Counter(arr[i][j] for i in range(_max_row) if arr[i][j] > 0).most_common(), 
                key=lambda p: (p[1], p[0]),
            )
            if not counter:
                break

            for i, (num, cnt) in enumerate(counter):
                if i >= 50:
                    break
                arr[2 * i][j] = num
                arr[2 * i + 1][j] = cnt
            else:
                for ii in range(2 * (i + 1), _max_row):
                    arr[ii][j] = 0

            max_row = max(max_row, 2 * (i + 1))
else:
    if arr[r][c] == k:
        t += 1
    else:
        t = -1

print(t)
