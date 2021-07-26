# 문제: [BOJ 20154] 이 구역의 승자는 누구야?!
# 유형: 문자열
# 메모리/시간: 43668kb / 380ms

import sys

input = sys.stdin.readline

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = "32123333113133122212112221"
alpha_to_count = dict(zip(alpha, map(int, count)))  # 알파벳-획수 딕셔너리

# 입력
string = input().rstrip()

stack = [alpha_to_count[s] for s in string]  # 연산 과정 저장 스택
while True:
    # stack에 숫자 하나만 있다면
    if len(stack) == 1:
        # 반복을 종료한다
        break
    # 아니라면
    new_stack = []  # 연산 결과를 저장할 새 스택
    # 2개씩 끊어서 연산을 진행
    for i in range(0, len(stack) - 1, 2):
        # 연산 결과를 새 스택에 저장한다
        new_stack.append((stack[i] + stack[i + 1]) % 10)
    # 만약 요소가 홀수개라면
    if len(stack) % 2:
        # 한 명을 부전승으로 추가한다
        new_stack.append(stack[-1])
    # 스택을 갱신한다
    stack = new_stack

# 출력
if stack[-1] % 2:
    print("I'm a winner!")  # 결과값이 홀수
else:
    print("You're the winner?")  # 결과값이 짝수
