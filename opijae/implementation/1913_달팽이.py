import sys
input= sys.stdin.readline
n=int(input())
target=int(input())
arr=[[0] *n for _ in range(n)]
directions = [(1,0),(0,1),(-1,0),(0,-1)]
value =n*n
row=-1
col=0
change_direction=[n] # 얼마나 가야 방향을 바꾸는지
for i in range(n-1,0,-1): # 방향은 n, n-1, n-1, n-2,n-2 .... 1,1 식으로 된다
    change_direction.append(i)
    change_direction.append(i)

for i in range(len(change_direction)): #
    direction=directions[i%4] # 방향이 바뀜
    for j in range(change_direction[i]): # 현재 방향이 얼마나 유지될지 
        row+=direction[0] # 행,열 업데이트
        col+=direction[1]

        if target==value: # 정답을 찾았을 때
            target_index=(row+1,col+1)
        arr[row][col]=value # arr 업데이트
        value-=1 

for i in arr:
    print(*i)
print(*target_index)
