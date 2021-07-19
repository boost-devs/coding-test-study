n = int(input())
mat = [list(input()) for _ in range(n)]
now = [list(input()) for _ in range(n)]
answer = [['.'] * n for _ in range(n)]
dy = [-1,-1,-1,0,0,1,1,1]
dx = [-1,0,1,-1,1,-1,0,1]
star_lst = []
star_cnt = 0
for y in range(n):
    for x in range(n):
        if now[y][x] == 'x':
            cnt = 0
            for i in range(8):
                next_y = y + dy[i]
                next_x = x + dx[i]
                if next_y in range(n) and next_x in range(n):
                    if mat[next_y][next_x] == '*':
                        cnt +=1
            answer[y][x] = str(cnt)
            if mat[y][x] =='*':
                star_cnt +=1
        if mat[y][x] =='*':
            star_lst.append([y,x])

if len(star_lst) > 0 and star_cnt >0:
    for y,x in star_lst:
        answer[y][x] = '*'
        
for y in range(n):
    print(''.join(answer[y]))

