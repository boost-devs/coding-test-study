# 문제: [BOJ 11720] 숫자의 합
# 유형: 문자열
# 메모리/시간: 29200kb / 68ms

import sys

input = sys.stdin.readline

# 입력
_ = input()
nums = map(int, input().rstrip())

# 출력
print(sum(nums))
