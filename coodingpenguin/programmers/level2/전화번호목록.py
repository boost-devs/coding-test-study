def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        # 바로 뒤에 전화번호의 접두어가 앞의 전화번호인지 확인
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True