# 문제: [BOJ 20442] ㅋㅋ루ㅋㅋ
# 유형: 투포인터
# 메모리/시간: 156256kb / 2124ms
# 참고: https://chanu-ps.tistory.com/24

import sys

input = sys.stdin.readline


def count_number_of_k(word):
    left_k, right_k = [], []
    count = 0  # 왼쪽 K의 개수
    for i in range(len(word)):
        if word[i] == "K":
            count += 1
        else:
            left_k.append(count)
    count = 0  # 오른쪽 K의 개수
    for i in range(len(word) - 1, -1, -1):
        if word[i] == "K":
            count += 1
        else:
            right_k.append(count)
    right_k.reverse()
    return left_k, right_k


# 입력
word = input().rstrip()  # 문자열

# 기준인 R에 대해
left_k, right_k = count_number_of_k(word)  # 왼쪽/오른쪽에 있는 K의 개수

start, end = 0, len(left_k) - 1  # R을 가리키는 포인터
length = 0  # 최장 길이
while start <= end:
    length = max(length, end - start + 1 + 2 * min(left_k[start], right_k[end]))  # 갱신
    # 오른쪽 K의 개수가 많다면
    if left_k[start] < right_k[end]:
        # 왼쪽 K의 개수를 늘리기 위해
        # start를 이동
        start += 1
    # 왼쪽 K의 개수가 많다면
    else:
        # 오른쪽 K의 개수를 늘리기 위해
        # end를 이동
        end -= 1

# 출력
print(length)
