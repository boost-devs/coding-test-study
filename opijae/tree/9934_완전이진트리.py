import sys
from collections import defaultdict
input = sys.stdin.readline

l_dict=defaultdict(list)
def binary_search_recursion(layer, start, end, data): #이진 탐색
    mid = round((start + end) / 2) # 중앙값 설정
    l_dict[layer].append(data[mid]) # 현재 방문한 값을 dict[layer]에 저장
    if layer==n-1: # layer에 다달았으면 return
        return
    binary_search_recursion(layer+1, start, mid - 1, data) # layer하나 증가, 끝점을 mid-1로 재설정
    binary_search_recursion(layer+1, mid + 1, end, data) # layer하나 증가, 시작점을 mid+1로 재설정
n= int(input())
tree=[]
tree.extend(list( input().split()))
binary_search_recursion(0,0,len(tree)-1,tree)

for k,v in l_dict.items():
    print(' '.join(v))