# 문제: [BOJ 1181] 단어 정렬
# 유형: 문자열, 정렬
# 메모리/시간: 33812kb / 116ms

import sys

input = sys.stdin.readline

# 입력
n = int(input())  # 단어의 개수
words = list(set([input().rstrip() for _ in range(n)]))  # 단어 리스트

# 정렬
words.sort(key=lambda x: (len(x), x))

# 출력
for word in words:
    print(word)
