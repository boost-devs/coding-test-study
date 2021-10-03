# 문제: [BOJ 16508] 전공책
# 유형: 비트마스크, 완전 탐색
# 메모리/시간: 31726kb / 536ms
# 참고: https://has3ong.github.io/boj/boj-16508/

import sys

input = sys.stdin.readline
INF = int(1e9)


def has_word(word, titles, price):
    count = 0  # 단어 문자 처리 카운트
    for letter in word:
        # 이어진 제목에 문자가 있다면
        if letter in titles:
            count += 1
            # 중복 문자 처리를 위해 변환
            titles = titles.replace(letter, " ", 1)
            # 단어가 제목에 있다면
            if count == len(word):
                return price  # 총 가격 반환
    return INF


# 입력
t = input().strip()  # 만들고 싶은 단어
n = int(input())  # 전공책 수
books = []  # 책 리스트
for _ in range(n):
    price, title = input().split()
    books.append((int(price), title))  # (가격, 제목)

result = []  # 모든 조합에 대한 총 가격
# 모든 책 조합에 대해서
for i in range(1 << n):
    total_price = 0  # 총 가격
    book_titles = ""  # 이어진 제목들
    for j in range(n):
        # 조합에 있는 책이라면
        if (i & 1 << j) != 0:
            total_price += books[j][0]
            book_titles += books[j][1]
    # 단어가 이어진 제목들에 있는지 확인
    result.append(has_word(t, book_titles, total_price))

min_total_price = min(result)  # 최소 가격
if min_total_price == INF:
    print(-1)
else:
    print(min_total_price)
