import sys
input = sys.stdin.readline
arr = []
for _ in range(19):
    arr.append(list(map(int, input().split())))
directions = ((0,1),(1,1),(1,0),(-1,1)) # 보는 방향
directions1 = ((0,-1),(-1,-1),(-1,0),(1,-1)) # 이점을 이미 봤는지 확인용

def check(i,j,color):
    orig_i, orig_j = i,j
    ban_arr = [] # 방향 중 가지 말아야하는 방향
    for idx,(di,dj) in enumerate(directions1): # 이 방향으로 점을 봤는지 확인
        if 0<=i+di<19 and 0<=j+dj<19:
            if arr[i+di][j+dj] == color:
                ban_arr.append(idx)
    for idx,(di,dj) in enumerate(directions):
        if idx in ban_arr:
            continue
        cnt = 0
        i,j = orig_i, orig_j 
        while True:
            if 0<=i<19 and 0<=j<19:
                if arr[i][j] ==color: 
                    cnt +=1
                    i += di
                    j += dj
                else:
                    break
            else:
                break
        if cnt == 5:
            return True
    return False


for i in range(19):
    for j in range(19):
        if arr[i][j] == 1:
            if (check(i,j,1)):
                print(1)
                print(i+1,j+1)
                exit()
        elif arr[i][j] == 2:
            if (check(i,j,2)):
                print(2)
                print(i+1,j+1)
                exit()
print(0)