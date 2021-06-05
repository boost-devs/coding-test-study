###### 1181번: 단어 정렬
# https://www.acmicpc.net/problem/1181
# 메모리/시간: 36680KB / 124ms

import sys

input = sys.stdin.readline

N = int(input().rstrip())
_input = set([input().rstrip() for _ in range(N)])
_input_len = [len(x) for x in _input]
word_list = [[x, y] for x, y in zip(_input, _input_len)]
word_list.sort(key=lambda x: (x[1], x[0]))

for x in word_list:
    print(x[0])