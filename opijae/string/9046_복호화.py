# https://www.acmicpc.net/problem/9046
import sys
from collections import Counter
input=sys.stdin.readline
n=int(input())
for _ in range(n):
    # input이 들어오면 space, 줄바꿈 제거
    # Counter와 most_common(2)를 사용해 빈도수가 높은 상위 2개를 가져옴  단어가 하나일때는 하나만 가져온다
    char_dict=Counter(input().rstrip().replace(' ','')).most_common(2)

    # char_dict : [('a',2),('b',1)] 같은 형식으로 나옵니다. (문자, 빈도수)

    # 단어의 수가 1 이상이고 빈도수가 같으면 ? 출력
    if len(char_dict)>1 and char_dict[0][1]==char_dict[1][1]:
            print('?')
    else:
        print(char_dict[0][0])