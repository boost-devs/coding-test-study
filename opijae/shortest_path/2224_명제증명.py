import sys
from collections import defaultdict, deque
input = sys.stdin.readline
n=int(input())
proposition_dict = defaultdict(set) # 노드 연결 고리 dict (중복을 방지하기 위한 set)
total_char=set() # 유니크한 문자열 저장
for _ in range(n):
    _input = input().split()
    s,e= _input[0],_input[-1]
    if s== e: # 출발, 도착이 같으면 넘김
        continue
    proposition_dict[s].add(e) # 연결 고리 저장
    total_char.add(s) # 유니크한 문자열 저장
    total_char.add(e)
# total_char=list(total_char)
length=len(total_char)
arr=[[0] * length for _ in range(length)] # 인접 행렬 초기 세팅
sorted_total_char = sorted(total_char) # 문자열 순서로 출력하기 위한 정렬
char_index_dict={x:i for i,x in enumerate(sorted_total_char)} # 문자열 to index dict
cnt=0
for key,items in proposition_dict.items():
    for item in items:
        i,j=char_index_dict[key],char_index_dict[item] # 문자열의 index 알아 내기 위함, arr에는 A to z 까지 순서대로 인덱스가 정렬되어야된다.
        arr[i][j]=1
        cnt+=1
# 플로이드 마셜
for k in range(length): # 거쳐가는 점
    for i in range(length): # 출발점
        for j in range(length): # 끝점
            # 이미 간선있거나, i==j(대각선, 항상 0), i,k가 연결되어 있거나, k,j가 연결되었는지 확인
            if not arr[i][j] and not i==j and arr[i][k] and arr[k][j] : 
                arr[i][j]=1
                cnt+=1
print(cnt)
for i in range(length):
    for j in range(length):
        if arr[i][j]:
            print('{} => {}'.format(sorted_total_char[i],sorted_total_char[j]))