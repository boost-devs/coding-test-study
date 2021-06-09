import sys

def check_keyword(Data,Keyword):
    # 입력을 소문자로 맞춰줌
    keyword = Keyword.lower()
    data = Data.lower()

    # 알파벳만 추출
    new_data = ''
    for i in data:
        if i.isalpha():
            new_data+=i
    # 알파벳만 추출한 데이터에 keyword 있는지 확인
    if keyword in new_data:
        print(1)
    else:
        print(0)

if __name__ =='__miain':
    
    #input
    data = input()
    keyword = input()
    
    check_keyword(data,keyword)

    
    