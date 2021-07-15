n = int(input())
m = int(input())

mat = [[0]*n for _ in range(n)]
st = [0,0]
visit = [[0]*n for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
dir = 0
mat[0][0] = n**2
num = n**2 -1
x,y = 0,0
answer = dict()
answer[n**2] =[0,0]

while [x,y] != [n//2,n//2]:    

    next_x = x+dx[dir]
    next_y = y+dy[dir]
    
    if next_x in range(n) and next_y in range(n) and mat[next_y][next_x] == 0:
        mat[next_y][next_x] = num
    else:
        dir +=1
        dir = dir%4
        next_x = x+dx[dir]
        next_y = y+dy[dir]
        mat[next_y][next_x] = num
    answer[num] = [next_y,next_x]
    x,y = next_x,next_y
    num -=1

for i in range(n):
    for j in range(n):
        print(mat[i][j],end = ' ')
    print('')
print(answer[m][0]+1,answer[m][1]+1)
