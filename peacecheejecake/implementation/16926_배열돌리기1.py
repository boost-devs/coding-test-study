# https://www.acmicpc.net/problem/16926
# 배열 돌리기 1
# 34468 KB / 192 ms


from collections import deque


n, m, r = map(int, input().split())
a = [[int(aa) for aa in input().split()] for _ in range(n)]

for k in range(min(n, m) // 2):
    # 원형 큐 만들기
    layer = deque()
    layer.extend(a[k][k:m - k])
    for i in range(k + 1, n - k - 1):
        layer.append(a[i][m - k - 1])
    layer.extend(a[n - k - 1][m - k - 1:k:-1])
    for i in range(n - k - 1, k, -1):
        layer.append(a[i][k])

    # 시계 반대방향(=왼쪽)으로 회전
    layer.rotate(-r)

    # 회전 후의 원소로 갱신하기
    for i in range(k, m - k):
        a[k][i] = layer.popleft()
    for i in range(k + 1, n - k - 1):
        a[i][m - k - 1] = layer.popleft()
    for i in range(m - k - 1, k, -1):
        a[n - k - 1][i] = layer.popleft()
    for i in range(n - k - 1, k, -1):
        a[i][k] = layer.popleft()

for row in a:
    print(' '.join(map(str, row)))
    