import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
arr = [[5]*n for _ in range(n)]

first_feed = []
for _ in range(n):
    first_feed.append(list(map(int, input().split()))) # 겨울마다 양분채워주기

trees = [[[] for _ in range(n)] for _ in range(n)] # 각 칸마다 들어 있는 나무 수

# 나무 좌표들을 저장
for _ in range(m):
    x,y,z=map(int,input().split())
    trees[x-1][y-1].append(z)

for _ in range(k):
    for i in range(n):
        for j in range(n):
            if len(trees[i][j])<=0: continue
            trees[i][j].sort()
            idx = 0
            while idx < len(trees[i][j]):
                if trees[i][j][idx] <= arr[i][j]:
                    arr[i][j] -= trees[i][j][idx]
                    trees[i][j][idx] += 1
                    idx+=1
                else:
                    die = trees[i][j][idx:] # 오름 차순으로 되어 있기 때문에 한 나무가 안되면 뒤에 다 죽음
                    for tree in die:
                        arr[i][j]+=(tree//2) # 죽으면 죽은 땅에 양분 더하기
                    trees[i][j]=trees[i][j][:idx] # 죽은 나무 빼기
                    break
    for i in range(n):
        for j in range(n):
            cnt = 0 # 번식이 가능한 나무 수
            if trees[i][j]:
                for age in trees[i][j]:
                    if age % 5 ==0:
                        cnt+=1
            if cnt > 0:
                for di,dj in directions:
                    ni = i + di
                    nj = j + dj
                    if 0<=ni<n and 0<=nj<n:
                        for _ in range(cnt):
                            trees[ni][nj].append(1)
            arr[i][j]+=first_feed[i][j] # 겨울되니 양분 더하기
ans=0
for i in range(n):
    for j in range(n):
        ans+=len(trees[i][j])
print(ans)