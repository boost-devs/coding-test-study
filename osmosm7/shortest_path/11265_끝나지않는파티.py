import sys
input = sys.stdin.readline
n,m = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            mat[i][j] = min(mat[i][j],mat[i][k] + mat[k][j])
for _ in range(m):
    s,e,t = map(int,input().split())
    if mat[s-1][e-1] <= t:
        print('Enjoy other party')
    else:
        print('Stay here')
