# 문제: [BOJ 9046] 복호화
# 유형: 문자열, Counter
# 메모리/시간: 31864kb / 88ms

import sys
from collections import Counter

input = sys.stdin.readline

# 입력
t = int(input())  # 테스트케이스 개수
for _ in range(t):
    encoded = input().rstrip().replace(" ", "")  # 암호화된 문자열
    # 문자의 종류가 1개라면
    if len(set(encoded)) == 1:
        # 가장 많은 문자이므로 출력
        print(encoded[-1])
    # 아니라면
    else:
        counter = Counter(encoded).most_common(2)  # 상위 2개만 추출
        # 1, 2등의 문자가 같다면
        if counter[0][1] == counter[1][1]:
            # ? 출력
            print("?")
        # 아니라면
        else:
            # 1등 문자만 출력
            print(counter[0][0])
