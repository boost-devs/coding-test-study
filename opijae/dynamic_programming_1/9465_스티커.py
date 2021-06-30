import sys
input = sys.stdin.readline
t= int(input())
for _ in range(t):
    n=int(input())
    arr=[]
    arr.append(list(map(int, input().split())))
    arr.append(list(map(int, input().split())))
    arr[0][1]+=arr[1][0] # 두번째 열 값은 미리 계산
    arr[1][1]+=arr[0][0] # 두번째 열 값은 미리 계산
    for i in range(2,n):
        arr[0][i]+=max(arr[1][i-2],arr[1][i-1]) # 첫번째 줄에서는 두번째 줄의 값들을 확인
        arr[1][i]+=max(arr[0][i-2],arr[0][i-1]) # 두번째 줄에서는 첫번째 줄의 값들을 확인
    print(max(arr[0][-1],arr[1][-1]))