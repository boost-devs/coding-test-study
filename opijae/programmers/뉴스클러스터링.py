from collections import deque
def solution(str1, str2):
    answer = 0
    # 대문자로 변경
    str1=str1.upper()
    str2=str2.upper()
    str1_list=deque()
    str2_list=deque()
    # 두글자씩 끊으면서 알파벳 아닌건 거름
    for i in range(0,len(str1)-1):
        temp=str1[i:i+2]
        if temp.isalpha():
            str1_list.append(temp)
    for i in range(0,len(str2)-1):
        temp=str2[i:i+2]
        if temp.isalpha():
            str2_list.append(temp)
    same=0
    total=len(str1_list)+len(str2_list)
    for i in range(len(str1_list)):
        a=str1_list.popleft()
        # 같은게 있는지 확인
        if a in str2_list:
            str2_list.remove(a)
            same+=1
        else:
            str1_list.append(a)
    sum_len=total-same
    try:
        answer=same/sum_len*65536
    except:
        answer=65536
    return int(answer)