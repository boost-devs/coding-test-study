import sys
import os
input = sys.stdin.readline
n=int(input())
ext_dict={}
for _ in range(n):
    _,ext=os.path.splitext(input().rstrip()) # os.path를 이용해 split
    try:
        ext_dict[ext]+=1 # dict에 이밎 키가 있으면 ++
    except:
        ext_dict[ext]=1 # 없으면 만들기
for i,j in sorted(ext_dict.items(), key=lambda item: item[0]):
    print(i[1:],j)
