n = int(input())
dct = dict()
stud = []
for _ in range(n**2):
    lst = list(map(int,input().split()))
    dct[lst[0]] = lst[1:]
    stud.append(lst[0])

mat = [[0]*n for _ in range(n)]
dy = [-1,0,1,0]
dx = [0,1,0,-1]
for s in stud:
    bin_lst = []
    for y in range(n):
        for x in range(n):
            if mat[y][x] == 0:
                like = 0
                bin = 0
                for i in range(4):
                    next_y = y+dy[i]
                    next_x = x+dx[i]
                    if next_y in range(n) and next_x in range(n):
                        if mat[next_y][next_x] in dct[s]:
                            like += 1
                        else:
                            if mat[next_y][next_x] == 0:
                                bin +=1
                bin_lst.append([y,x,like,bin])
        
    bin_lst.sort(key = lambda x: [-x[2],-x[3],x[0]])
    now_y, now_x = bin_lst[0][0], bin_lst[0][1]
    mat[now_y][now_x] = s

answer = 0
for y in range(n):
    for x in range(n):
        now = mat[y][x]
        cnt = 0
        for i in range(4):
            next_y = y+dy[i]
            next_x = x+dx[i]
            if next_y in range(n) and next_x in range(n):
                if mat[next_y][next_x] in dct[now]:
                    cnt+=1
        if cnt ==0:
            continue
        answer += 10**(cnt-1)
print(answer)