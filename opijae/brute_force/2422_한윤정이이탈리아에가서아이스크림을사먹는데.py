from itertools import combinations
from collections import defaultdict
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
ban_dict = defaultdict(list)
for _ in range(m):
    a,b = map(int, input().split())
    ban_dict[a].append(b)
    ban_dict[b].append(a)
combs = combinations(range(1,n+1),3)
cnt =0
for comb in combs:
    a,b,c = comb
    if b in ban_dict[a] or c in ban_dict[a] or b in ban_dict[c]: # 세 수 a,b,c가 금지조합에 있는지 확인한다.
        continue
    cnt += 1
print(cnt)