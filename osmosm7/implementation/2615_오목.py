import sys
def dfs(num,y,x,dir):
    global cnt
    if y+dir[0] in range(19) and x+dir[1] in range(19):
        if mat[y+dir[0]][x+dir[1]] == num:
                cnt +=1
                dfs(num,y+dir[0],x+dir[1],dir)
        else:
            return
    else:
        return
    
mat = [list(map(int,input().split())) for i in range(19)]

dir = [[1,0],[1,1],[0,1],[-1,1]]
for i in range(19):
    for j in range(19):
        if mat[i][j] != 0:
            num = mat[i][j]
            for n in range(4):
                if i+dir[n][0] in range(19) and j+dir[n][1] in range(19):
                    if mat[i+dir[n][0]][j+dir[n][1]] == num:
                        if i-dir[n][0] in range(19) and j-dir[n][1] in range(19) and mat[i-dir[n][0]][j-dir[n][1]] == num:
                            continue
                        cnt = 1
                        dfs(num,i,j,dir[n])
                        if cnt ==5:
                            print(num)
                            print(i+1,j+1)
                            sys.exit(0)
print(0)