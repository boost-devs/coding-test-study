# 문제: [BOJ 4659] 비밀번호 발음하기
# 유형: 문자열
# 메모리/시간: 29200kb / 64ms

import sys

input = sys.stdin.readline
vowels = ["a", "e", "i", "o", "u"]


def check(password):
    length = len(password)
    has_vowel = [letter in vowels for letter in password]
    # 모음을 포함하지 않는 경우
    if not any(has_vowel):
        return False
    for i in range(1, length):
        # e, o 빼고 같은 문자가 두 번 반복되는 경우
        if (password[i - 1] == password[i]) and (password[i] not in "eo"):
            return False
        if i > 1:
            patch = has_vowel[i - 2 : i + 1]
            # 모음 or 자음이 연속 3개 오는 경우
            if all(patch) or not any(patch):
                return False
    return True


while True:
    # 입력
    password = input().rstrip()  # 비밀번호
    if password == "end":
        # 종료
        break

    # 출력
    if check(password):
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")
