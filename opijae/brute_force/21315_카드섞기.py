import sys
import math
from itertools import product,combinations
from collections import deque
input = sys.stdin.readline
n = int(input())
target = list(map(int, input().split()))
max_k = int(math.log(n, 2))
prods = product(range(1,max_k+1),repeat=2) # k의 조합

def shuffle(n,cards):
    shuffle_range = 2**n # 2**k+1-i
    arr = deque() # 셔플 불가능한 카드들
    can_shuffle = cards # 셔플 가능한 카드들
    while shuffle_range>0:
        temp = []
        arr.extendleft(can_shuffle[:-shuffle_range][::-1]) # extendleft로 넣으면 arr = [1], can_shuffle[:-shuffle_range] = [2,3] => [3,2,1]로되서 reverse한 다음 넣어야된다.
        can_shuffle = can_shuffle[-shuffle_range:] # 셔플 할수 있는 카드 목록 업데이트
        temp.extend(can_shuffle)
        temp.extend(arr)
        shuffle_range //= 2
    return temp
for first,second in prods:
    cards = list(range(1,n+1))
    if shuffle(second,shuffle(first,cards)) == target:
        print(first,second)
        break

