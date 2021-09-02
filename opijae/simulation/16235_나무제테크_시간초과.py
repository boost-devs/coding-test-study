import sys
from collections import deque
input = sys.stdin.readline

n,m,k = map(int,input().split())
directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

arr = [[5]*n for _ in range(n)]
dead_trees = [[0]*n for _ in range(n)] # 올해에 죽는 나무의 영양분 배열
first_feed = []
for _ in range(n):
    first_feed.append(list(map(int, input().split())))
trees = []

for _ in range(m):
    _input = list(map(int, input().split() ))
    trees.append([_input[0]-1, _input[1]-1,_input[2]])

trees = sorted(trees, key= lambda x: x[2])  # 나무 나이에 맞게 정렬
trees = deque(trees)
for i in range(k):
    length = len(trees)
    temp = []
    # 봄, 여름, 가을 
    for _ in range(length):
        i,j,age = trees.popleft()
        if arr[i][j] >= age:  # 봄에는 나무가 자라고
            arr[i][j] -= age
            trees.append([i,j,age+1])
            if (age + 1) % 5 == 0: # 가을에 번식할 나무
                for di,dj in directions:
                    ni = i + di
                    nj = j + dj
                    if 0<= ni < n and 0 <= nj < n:
                        temp.append([ni,nj,1])
        else: # 여름에 죽어서 양분을 줄 나무
            dead_trees[i][j] += age//2
    if not trees: # 나무가 한그루도 없으면 종료
        print(0)
        sys.exit()
    trees.extendleft(temp)

    for i in range(n):
        for j in range(n):
            arr[i][j] += (first_feed[i][j] + dead_trees[i][j]) # 여름에 죽은 나무 양분 + 겨울에 주는 양분
            dead_trees[i][j] = 0

print(len(trees))
