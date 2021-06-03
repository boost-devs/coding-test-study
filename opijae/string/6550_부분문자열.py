import sys
input= sys.stdin.readline

while True:
    line=input().split()
    if not line:  # 입력이 더 없으면 종료
        break
    idx=0
    # line[0] : s , line[1] : t
    for s in line[1]:
        if line[0][idx]==s:
            line[0]=line[0][1:] # s의 문자가 t안에 있다면 앞에사 부터 하나씩 뻄
        if len(line[0])==0: # s의 길이가 0이면 모든 문자가 t안에 있으니 break
            print('Yes')
            break
    else:
        print('No')