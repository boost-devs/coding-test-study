# https://www.acmicpc.net/problem/10994
# 별 찍기 - 19
# 29592 KB / 124 ms


n = int(input())

l = 4 * (n - 1) + 1
sky = [[' '] * l for _ in range(l)]
m = l // 2
for i in range(l):
    for j in range(l):
        if (
            i % 2 == 0 and abs(m - j) <= abs(m - i) or
            j % 2 == 0 and abs(m - i) <= abs(m - j)
        ):
            sky[i][j] = '*'

    print(''.join(sky[i]))
