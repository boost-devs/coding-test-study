import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(map(int, input().split()))
_min =10000000000
for i in range(n-3): # 시작점 -> 뒤에 최소 3개가 더 있어야되니 n-3까지 간다.
    for j in range(i+3,n): # 끝점 -> 앞에 최소 3개가 필요하니 i +3 부터 시작
        left = i + 1
        right = j - 1
        while left < right:
            _diff = arr[i] + arr[j] -arr[left] -arr[right] # 현재 두 눈사람의 차
            if _diff >0: # 차가 0보다 크면 left를 늘림
                left += 1
            else:
                right -= 1
            if _min > abs(_diff):
                _min = abs(_diff)
print(_min)