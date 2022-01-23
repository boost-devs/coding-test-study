def solution(phone_book):
    # phone book을 글자와, 길이순으로 정렬(자동으로 됨)
    phone_book.sort()
    for i in range(len(phone_book)-1):
        # 현재 값이 그 다음 값의 접두사인지 확인
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False

    return True