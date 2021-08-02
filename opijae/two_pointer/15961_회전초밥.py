import sys
input = sys.stdin.readline

n,d,k,c = map(int, input().split())
check = [0] * (d+1) # 초밥을 먹는지 체크
sushi_arr =[]
for _ in range(n):
    sushi_arr.append(int(input()))
check[c] = 1 # 서비스는 먹었다고 친다.
cnt =1 
_max =0 
for i in range(k): # 처음 k개를 먹었을 때 
    check[sushi_arr[i]] += 1 # 체크 ++ 
    if check[sushi_arr[i]] == 1: # 체크가 1이면 한 종류의 초밥이 있다는 뜻임
        cnt += 1
for i in range(k,n+k):
    if i>=n:
        i -= n # '회전' 초밥
    check[sushi_arr[i-k]] -= 1 # 왼쪽 값 뺴기
    if check[sushi_arr[i-k]] == 0 : # 0 이면 안먹은게 되니 cnt --
        cnt -= 1
    check[sushi_arr[i]] += 1 #오른쪽 값 더하기
    if check[sushi_arr[i]] == 1 : 
        cnt += 1
    _max = max(cnt, _max)
print(_max)