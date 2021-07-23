import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n, d = map(int, input().split())

    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    crisp = [] # 껍질(밖)정보를 저장하는 배열
    cnt = 0
    for _ in range(n//2): # 8방향 정보 배열에 저장
        crisp.append([
            arr[cnt][cnt], arr[n//2][cnt], arr[n-1-cnt][cnt],
            arr[n-1-cnt][n//2], arr[n-1-cnt][n-1-cnt],
            arr[n//2][n-1-cnt], arr[cnt][n-1-cnt], arr[cnt][n//2]
        ])
        cnt += 1
    d = ((d+360)//45) % 8 # 몇번 돌릴지 정하기

    # 돌릴 만큼 돌리기 [1,2,3] -> [3,2,1]
    for i in range(len(crisp)-1):
        temp = crisp[i][:d]
        crisp[i] = crisp[i][d:]
        crisp[i].extend(temp)

    cnt = 0
    # 돌려진 배열을 원 배열 위취에 맞춰 넣기
    for i in range(n//2):
        arr[cnt][cnt], arr[n//2][cnt], arr[n-1-cnt][cnt], arr[n-1-cnt][n//2], arr[n-1 -
                                                                                  cnt][n-1-cnt], arr[n//2][n-1-cnt], arr[cnt][n-1-cnt], arr[cnt][n//2] = crisp[i]
        cnt += 1
    for a in arr:
        print(*a)
