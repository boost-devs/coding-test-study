# https://www.acmicpc.net/problem/17276
# 배열 돌리기
# 39132 KB / 800 ms


def rotate(n, d):
    x = [
        [int(xx) for xx in input().split()] 
        for _ in range(n)
    ]
    
    if d == 0 or d == 360:
        return x

    axes = [
        (x[n - 1 - i][i], x[n // 2][i], x[i][i], x[i][n // 2])
        for i in range(n)
    ]

    for i in range(n):
        starts = [
            (n - 1 - i, i), (n // 2, i), (i, i), (i, n // 2),
        ]
        for s, (r, c) in enumerate(starts):
            rev, s_org = divmod((s - d // 45) % 8, 4)
            j = n - 1 - i if rev == 1 else i
            x[r][c] = axes[j][s_org]

    return x


def pprint(arr):
    for row in arr:
        print(' '.join(map(str, row)))


for _ in range(int(input())):
    n, d = map(int, input().split())
    pprint(rotate(n, d))
