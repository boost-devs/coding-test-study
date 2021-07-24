# 문제: [BOJ 17413] 단어뒤집기 2
# 유형: 구현
# 메모리/시간: 29452kb / 76ms

import sys

input = sys.stdin.readline


def get_bracket_position(string):
    left_bracket, right_bracket = [], []
    for i in range(len(string)):
        if string[i] == "<":
            left_bracket.append(i)
        if string[i] == ">":
            right_bracket.append(i)
    return left_bracket, right_bracket


def reverse_non_tagged(string):
    return " ".join([word[::-1] for word in string.split()])


def reverse_string(string):
    left_bracket, right_bracket = get_bracket_position(string)  # 왼쪽 괄호와 오른쪽 괄호 인덱스
    # 괄호가 없다면
    if not left_bracket:
        return reverse_non_tagged(string)

    # 괄호가 있다면
    result = ""  # 최종 변환 문자열

    # 맨 앞 괄호 이전 문자열은
    if left_bracket[0] > 0:
        # 뒤집는다
        result += reverse_non_tagged(string[: left_bracket[0]])

    # 맨 앞 괄호부터 맨 끝 괄호까지의 문자열은
    for i in range(len(left_bracket)):
        # 왼쪽 괄호와 오른쪽 괄호 사이는 그대로 가져온다
        result += string[left_bracket[i] : right_bracket[i] + 1]
        # 오른쪽 괄호와 왼쪽 괄호 사이는 태그가 아닌 문자열이므로
        if i + 1 < len(left_bracket):
            # 뒤집는다
            result += reverse_non_tagged(
                string[right_bracket[i] + 1 : left_bracket[i + 1]]
            )

    # 맨 끝 괄호 이후 문자열은
    if right_bracket[-1] < len(string) - 1:
        # 뒤집는다
        result += reverse_non_tagged(string[right_bracket[-1] + 1 :])

    return result


s = input().strip()  # 뒤집을 문자열
print(reverse_string(s))
