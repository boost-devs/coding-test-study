###### 4659번: 비밀번호 발음하기
# https://www.acmicpc.net/problem/4659
# 메모리/시간: 32108KB / 88ms

import sys
from collections import deque

input = sys.stdin.readline

aeiou = ('a', 'e', 'i', 'o', 'u')

while True:
    _input = input().rstrip()
    if _input == "end":
        break
    password = deque(_input)
    cond1, cond2, cond3 = False, True, True
    ck_cond2, ck_cond3 = [], ""
    
    while password:
        x = password.popleft()
        if not cond1:
            if x in aeiou:
                cond1 = True

        if cond2:
            if x in aeiou:
                if len(ck_cond2) == 0:
                    ck_cond2 = [x]
                else:
                    if ck_cond2[0] in aeiou:
                        ck_cond2.append(x)
                    else:
                        ck_cond2 = [x]

            else:
                if len(ck_cond2) == 0:
                    ck_cond2 = [x]
                else:
                    if ck_cond2[0] in aeiou:
                        ck_cond2 = [x]
                    else:
                        ck_cond2.append(x)

            if len(ck_cond2) >= 3:
                cond2 = False

        if cond3:
            if x == ck_cond3:
                if (x == 'e') or (x == 'o'):
                    continue
                else:
                    cond3 = False

            else:
                ck_cond3 = x

    print(f"<{_input}> is acceptable.") if all([cond1, cond2, cond3]) else print(f"<{_input}> is not acceptable.")