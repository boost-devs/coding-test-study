import sys
input = sys.stdin.readline
n=int(input())
arr=list(map(int, input().split())) # 배열 저장
for i in range(1,n):
    arr[i]=max(arr[i],arr[i]+arr[i-1]) # 연속된 수니 이전 값과 현재 값을 더한 것 중 최대값 고르기
print(max(arr))