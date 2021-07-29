import sys
input = sys.stdin.readline
n,x = map(int, input().split())
arr = list(map(int, input().split()))
_sum = -10000
_max = -10000
for i in range(n-x+1):
    if _sum < 0:
        _sum = sum(arr[:x]) # 시작할떄는 sum 해줌
    else:
        _sum += (arr[i+x-1]-arr[i-1]) # 한칸씩 밀면서 왼쪽꺼 빼주고 오른쪽꺼는 더해줌 
    if _sum > _max:
        _max = _sum
        cnt = 1
    elif _sum == _max:
        cnt += 1
if _max == 0:
    _max = 'SAD'
    print(_max)
else:
    print(_max)
    print(cnt)