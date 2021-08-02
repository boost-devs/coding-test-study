import sys
input = sys.stdin.readline

n,s = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right =1
_min= 10000000
cur_sum = arr[0]
while left < n:
    if cur_sum < s:
        if right >= n:
            break
        cur_sum += arr[right]
        right += 1
    else:
        _min = min(_min,right-left)
        cur_sum -= arr[left]
        left += 1
if _min == 10000000:
    print(0)
else:
    print(_min)
