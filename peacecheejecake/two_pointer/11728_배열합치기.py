# https://www.acmicpc.net/problem/11728
# 배열 합치기
# 185644 KB / 2788 ms


def readline():
    return tuple(map(int, input().split()))

n, m = readline()
a = readline()
b = readline()

i, j = 0, 0
while i + j < n + m:
    if i == n:
        print(' '.join(map(str, b[j:])))
        break
    if j == m:
        print(' '.join(map(str, a[i:])))
        break

    if a[i] <= b[j]:
        num = a[i]
        i += 1
    else:
        num = b[j]
        j += 1
    print(num, end=' ')
