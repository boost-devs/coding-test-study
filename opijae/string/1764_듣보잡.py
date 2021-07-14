import sys
from collections import OrderedDict
input = sys.stdin.readline

no_listen,no_see= map(int, input().split())
no_list_dict={} # 듣지 못한 dict
no_listen_see_list=[] # 듣보 list
for i in range(no_listen):
    no_list_dict[input().rstrip()]=1 # 듣지 못한 dict에 값 채우기
# print(no_list_dict)
for _ in range(no_see):
    people=input().rstrip()
    try:
        _=no_list_dict[people] # 듣지 못한 dict에 값이 있으면 다음 step
    except: # 없으면 넘어감
        continue
    no_listen_see_list.append(people) # 듣보 list에 업데이드
print(len(no_listen_see_list)) # 이걸 확인을 못했다..
for people in sorted(no_listen_see_list):
    print(people)
