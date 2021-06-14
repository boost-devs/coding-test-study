# https://www.acmicpc.net/problem/9934
# OBILAZAK

K = int(input())
paper = list(map(int, input().split()))

indices = [
    [j * 2 ** (K - i) - 1 for j in range(1, 2 ** i, 2)] 
    for i in range(1, K + 1)
]

for idx in indices:
    for i in idx:
        print(paper[i], end=" ")
    print()