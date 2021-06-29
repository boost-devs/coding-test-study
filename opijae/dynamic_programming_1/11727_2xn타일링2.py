import sys
input = sys.stdin.readline

n= int(input())
arr=[1,1,3] # arr[0]은 padding
for i in range(3,n+1):
    arr.append(arr[-1]+arr[-2]*2) # 그 전 값이랑 그 전전 값(가로로 두었을 때 == 2*2 타일) *2 를 더함
print(arr[n]%10007)
