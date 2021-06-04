import sys
input = sys.stdin.readline

aeiou='aeiou'
while True:
    string=input().rstrip()
    if string=='end': # end가 입력되면 종료
        break
    aeiou_cnt=0 # 연속된 모음의 수
    not_aeiou_cnt=0 # 연속된 자음의 수
    prev_str='' # 이전 문자
    is_accept=True # 문장이 조건에 성립되는지?
    is_aeiou=False # 모음이 있는지
    for s in string:
        if s!='e'and s!='o' and s==prev_str: # e랑 o가 아니고 이전 글자랑 같으면 
            is_accept=False
            break
        if s in aeiou: # 모음이라면 
            is_aeiou=True # 모음조건 True
            aeiou_cnt+=1 #연속 모음 ++
            not_aeiou_cnt=0 # 연속 자음 0으로 만듬
            if (prev_str=='e' and s=='e') or (prev_str=='o' and s=='o'): # e나 o이면 모음에 안낌
                aeiou_cnt-=1
        else:
            not_aeiou_cnt+=1 # 자음 개수 ++
            aeiou_cnt=0 # 연속모음 0으로
        if aeiou_cnt>2 or not_aeiou_cnt>2: # 모음이나 자음이 3개 이상 연속 되었으면
            is_accept=False
            break
        prev_str=s
    if is_accept and is_aeiou:
        print('<{}> is acceptable.'.format(string))
    else:
        print('<{}> is not acceptable.'.format(string))