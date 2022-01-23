def solution(phone_book):
    n = len(phone_book)
    memo = [""] * n
    for l in range(20):
        for i in range(n):
            memo[i] += phone_book[l]

        if len(set(memo)) < n:
            return False

    return True
