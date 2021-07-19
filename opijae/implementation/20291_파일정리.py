import sys
from collections import defaultdict
input = sys.stdin.readline
n=int(input())

ext_dict = defaultdict(int)

for _ in range(n):
    ext_dict[input().rstrip().split('.')[-1]]+=1 # 확장자 찾고 개수 ++
for ext, cnt in sorted(ext_dict.items(), key= lambda x:x[0] ): # 확장자 순으로 정렬
    print(ext,cnt)
