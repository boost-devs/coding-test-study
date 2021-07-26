import sys
input = sys.stdin.readline

def is_group_word(string):
    str_list=[0] # index 에러 날까바 0을 넣고 시작
    for s in string: # 한글자씩 확인
        if s!=str_list[-1]: # str_list에 최근에 들어간 글자랑 현재글자가 다르면 새로운 글자로 판단
            str_list.append(s)
        if s in str_list[:-1]: # 제일 최근 글자 제외한 리스트안에 s가 있으면 중복된 글씨니 return False
            return False
    return True

n= int(input())
ans=0
for _ in range(n):
    if is_group_word(input().rstrip()):
        ans+=1
print(ans)