# 문제: [BOJ 16719] ZOAC
# 유형: 구현, 재귀
# 메모리/시간: 29200kb / 72ms
# 참고: https://hillier.tistory.com/109

import sys

input = sys.stdin.readline


def check_word(start, word):
    if not word:
        return
    letter = min(word)
    pos = word.index(letter)
    arr[start + pos] = letter
    print("".join(arr))

    check_word(start + pos + 1, word[pos + 1 :])
    check_word(start, word[:pos])


word = input().rstrip()
arr = [""] * len(word)
check_word(0, word)
