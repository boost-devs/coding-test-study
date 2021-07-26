# 문제: [BOJ 12933] 오리
# 유형: 구현, 문자열
# 메모리/시간: 29200kb / 160ms

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
    # 처리한 적 없는 시작점이라면
    if not visited[s]:
        point = 0  # 오리 소리가 들리는 지점
        for i in range(s, l):
            # 들려야 하는 소리와 같고 처리한 적 없는 지점이라면
            if record[i] == sound[point % 5] and not visited[i]:
                visited[i] = True  # 처리 여부 체크
                point += 1  # 다음 지점으로 이동
        # k로 끝났다면
        if not point % 5:
            count += 1  # 오리 수 증가
        # 아니라면
        else:
            # 잘못된 울음소리이므로 break
            imcomplete = True
            break

if imcomplete or not all(visited):
    print(-1)
else:
    print(count)
