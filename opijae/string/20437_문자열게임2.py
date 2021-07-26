import sys
import re
input = sys.stdin.readline
n= int(input())
for _ in range(n):
    string=input().rstrip()
    num=int(input())
    set_string=set(string) # set을 이용해 unique  문자들만 가져옴
    _max,_min=0,100000
    for s in set_string:
        match_iters=re.finditer(s, string) # 정규식을 사용해 target 위치 찾기 match_iters => iterater, <_sre.SRE_Match object; span=(1 시작점, 2 끝점), match='a'>
        match_list_idx=[x.start() for x in match_iters] # target위치의 시작점들만 저장
        cnt=0
        if len(match_list_idx) >=num: # target의 개수가 num보다 크면
            while True:
                diff=match_list_idx[cnt+num-1]-match_list_idx[cnt] # 제일 앞 글자, 뒤글자의 차
                if _min>diff:
                    _min=diff
                if _max<diff:
                    _max=diff
                cnt+=1
                if cnt+num>len(match_list_idx): #앞글자 index ++
                    break
    if _max+_min==100000:
        print(-1)
    else:
        print(_min+1,_max+1)
