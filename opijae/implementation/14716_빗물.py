import sys
input = sys.stdin.readline

h,w = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(w):
    max_left = max(arr[:i+1]) # 현재 기준 왼쪽으로 높은 건물
    max_right = max(arr[i:])  # 현재 기준 오른쪽으로 높은 건물
    stand = min(max_left, max_right) # 둘중 작은거(작은거 기준으로 물이 참)
    ans += stand-arr[i] # 빗물 양 계산
print(ans)  