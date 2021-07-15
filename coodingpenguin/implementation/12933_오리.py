# 문제: [BOJ 12933] 오리
# 유형: 구현, 문자열
# 메모리/시간: 67660kb / 772ms

import sys

input = sys.stdin.readline

record = input().rstrip()  # 녹음한 소리
l = len(record)  # 소리의 길이
sound = "quack"  # 오리 울음소리

starts = [i for i in range(l) if record[i] == "q"]  # 오리 울음소리 시작지점 후보
visited = [False] * l  # 소리 처리 여부

count = 0  # 오리 마리수
imcomplete = False  # 문자가 부족한 경우
while starts:
    s = starts.pop(0)
    if not visited[s]:
        point = 0
        for i in range(s, l):
            if record[i] == sound[point % 5] and not visited[i]:
                visited[i] = True
                point += 1
        if not point % 5:
            count += 1
        else:
            imcomplete = True
            break

if imcomplete or not all(visited):
    print(-1)
else:
    print(count)
