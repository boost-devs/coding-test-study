import sys
from collections import defaultdict, deque
input =sys.stdin.readline
n = int(input())

arr = []
directions = ((-1,0),(1,0),(0,1),(0,-1))

for i in range(n):
    _input = list(map(int, input().split()))
    temp = []
    for j in range(n):
        temp.append(_input[j])
        if _input[j] == 9:
            si,sj = i,j
            temp[j] = 0 # 시작 지점을 0으로 바꿔주기
    arr.append(temp)
fish_size = 2 # 물고기 크기;
move_num = 0 # 이동 횟수
eat_cnt = 0 # 먹은 물고기 수
while True:
    q =deque([[si,sj,0]])  # 시작점 넣기
    visited = [[False]*n for _ in range(n)]
    flag = 10000000 # 움직인 횟수 보다 큰지 비교
    fish = []

    while q:
        # print(q)
        i, j , cnt = q.popleft()

        if cnt > flag:
            break
        for di,dj in directions:
            ni = i + di
            nj = j + dj

            if (
                0<= ni < n and
                0<= nj < n and
                not visited[ni][nj] and
                arr[ni][nj] <= fish_size
            ):
                if 0 < arr[ni][nj] < fish_size: # 물고기를 먹을 수 있으면 
                    fish.append([ni,nj,cnt+1])
                    flag = cnt
                visited[ni][nj] = True
                q.append([ni,nj,cnt + 1])
    if len(fish) > 0: # 물고기를 먹었다면
        fish.sort() # 왼쪽위, 가까운 물고기
        i ,j ,move_cnt = fish[0]
        move_num += move_cnt
        eat_cnt += 1
        if eat_cnt == fish_size:
            fish_size += 1
            eat_cnt = 0
        arr[i][j] = 0
        si,sj = i,j
    else:
        break
print(move_num)
