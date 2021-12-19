from collections import defaultdict
n = int(input())
mat = [list(map(int,input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1 or (mat[i][k] ==1 and mat[k][j] ==1): 
                mat[i][j] =1

for i in range(n):
    for j in range(n):
        print(mat[i][j],end = ' ')
    print()                    