import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(map(int, input().split()))
_min = 100000000000000000
left ,right =0,n-1 # 왼쪽 인덱스, 오른쪽 인덱스
_left ,_right =0,0 # 0에 제일 가까울떄 왼쪽, 오른쪽 인덱스
while left < right:
    temp = arr[left]+arr[right]
    if  abs(temp) < _min:
        _min = abs(temp)
        _left = left
        _right = right
    if temp>0: # 왼쪽으로 한칸 이동
        right -= 1
    elif temp<0 : # 오른 쪽으로 한칸 이동
        left += 1
    else: # 0 이면 멈춤
        break
print(arr[_left],arr[_right])
