# 문제: [BOJ 11365] !밀비 급일
# 유형: 문자열
# 메모리/시간: 29200kb / 72ms

import sys

input = sys.stdin.readline

while True:
    # 입력
    encoded = input().rstrip()
    # END라면
    if encoded == "END":
        # 해독 중지
        break
    # 출력
    print(encoded[::-1])
