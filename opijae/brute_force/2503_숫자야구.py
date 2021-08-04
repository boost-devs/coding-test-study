import sys
from itertools import permutations
input = sys.stdin.readline

n= int(input())
candi = list(permutations(['1','2','3','4','5','6','7','8','9'],3)) # 후보군 구하기
ans =0
for _ in range(n):
    num,s,b = map(int, input().split())
    str_num = str(num)
    str_num[0]
    cnt = 0
    if s == 3:
        break
    for i in range(len(candi)):
        strike,ball =0,0
        i -= cnt # 배열을 지우니 index 맞춰줌
        for j in range(3):
            if candi[i][j] == str_num[j]: # 자리수와 숫자가 같은면 스트라이크
                strike += 1
            elif str_num[j] in candi[i]: # 숫자만 같으면 볼
                ball += 1
        if (strike!=s) or (ball!=b): # 스트라이크라 볼 갯수가 같은지 확인
            candi.pop(i) # 다르면 후보군에서 제외
            cnt += 1
if s == 3:
    print(1)
else:
    print(len(candi))