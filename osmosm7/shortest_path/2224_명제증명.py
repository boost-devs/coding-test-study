from collections import defaultdict
n = int(input())
mat_len = (ord('z') - ord('A')+1)
mat = [[0] * mat_len for _ in range(mat_len)]
for _ in range(n):
    a,b = input().split(' => ')
    a = ord(a) - ord('A')
    b = ord(b) - ord('A')
    mat[a][b] = 1

for k in range(mat_len):
    for i in range(mat_len):
        for j in range(mat_len):
            if mat[i][j] ==1 or (mat[i][k] ==1 and mat[k][j] ==1):
                mat[i][j] =1

cnt = 0
for i in range(mat_len):
    for j in range(mat_len):
        if i == j:
            mat[i][j] =0
        if mat[i][j] ==1:
            cnt+=1
print(cnt)
for i in range(mat_len):
    for j in range(mat_len):
        if mat[i][j] ==1:
            print(chr(i+ ord('A'))+' => '+chr(j+ ord('A')))