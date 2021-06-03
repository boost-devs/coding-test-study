# https://www.acmicpc.net/problem/10798
import sys
input=sys.stdin.readline

str_list=[]
max_len=-100
for _ in range(5):
    temp=input().rstrip() 
    if len(temp)>max_len: # 최대 길이 저장
        max_len=len(temp)
    str_list.append(temp) # str_list에 입력값들 저장

# 리스트에 접근 할때 j, i 순서로 접근
for i in range(max_len):
    for j in range(5):
        if len(str_list[j])<=i: # str길이가 고갈되면 pass
            pass
        else:
            print(str_list[j][i],end='') # 아니면 출력
