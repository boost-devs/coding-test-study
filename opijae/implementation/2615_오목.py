import sys

input = sys.stdin.readline

direction = [(0,1),(1,0),(1,-1),(1,1)]
black = []
white = []

for i in range(1,20):
    board = list(map(int,input().split()))
    for j in range(len(board)):
        if board[j] == 1:
            black.append((i,j+1))
        elif board[j] == 2:
            white.append((i,j+1))
print(black)
def check(i,j,d):
    global cnt
    print(i,j,d)
    if (i,j+1) in black and (d==0 or d==1):
        cnt +=1
        check(i,j+1,1)
    if (i+1,j) in black and (d==0 or d==2):
        cnt +=1
        check(i+1,j+1,2)
    if (i+1,j-1) in black and (d==0 or d==3):
        cnt +=1
        check(i+1,j-1,3)
    if (i+1,j+1) in black and (d==0 or d==4):
        cnt +=1
        check(i+1,j+1,4)
    return cnt
for i,j in black:
    cnt= 1
    print(i,j,100)
    check(i,j,0)
    if cnt ==5:
        print(1)
        print(i,j)
        sys.exit()
for i,j in white:
    cnt= 1
    check(i,j)
    if cnt ==5:
        print(2)
        print(i,j)
        sys.exit()
print(0)
