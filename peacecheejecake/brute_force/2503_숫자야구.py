# https://www.acmicpc.net/problem/2503
# 숫자 야구
# 33292 KB / 184 ms


from itertools import permutations
from string import digits


def check_count(guess, answer):
    strike, ball = 0, 0
    for g, a in zip(guess, answer):
        if g == a:
            strike += 1
        elif g in answer:
            ball += 1
    return strike, ball


N = int(input())

memory = {
    ''.join(p): True for p in permutations(digits[1:], 3)
}
for _ in range(N):
    guess, count = input().split(maxsplit=1)
    strike, ball = map(int, count.split())
    for cand in memory:
        if check_count(guess, cand) != (strike, ball):
            memory[cand] = False

print(sum(memory.values()))
