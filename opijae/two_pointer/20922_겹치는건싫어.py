import sys
from collections import defaultdict
input = sys.stdin.readline
n,k = map(int, input().split())
arr = list(map(int, input().split()))
_max = 0
n_dict = defaultdict(int) # 현재 구간에 있는 숫자 count
left_idx = 0
for i in range(n):
    n_dict[arr[i]] += 1
    if n_dict[arr[i]] == k+1:
        while True:
            if arr[left_idx] == arr[i]:
                n_dict[arr[left_idx]] -= 1 
                left_idx += 1
                break
            n_dict[arr[left_idx]] -= 1  # 왼쪽 포인터 결과값 하나씩 뺴기
            left_idx += 1
    _max =  max((i - left_idx),_max)
print(_max+1)