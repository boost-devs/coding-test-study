import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    word = input().rstrip()
    l = len(word)
    # print([word[i] == [i for i in range(len(word//2))])
