# 문제: [BOJ 3029] 경고
# 유형: 문자열
# 메모리/시간: 29200kb / 68ms

import sys

input = sys.stdin.readline

# 입력
_ = input()
nums = map(int, input().rstrip())

# 출력
print(sum(nums))
