import sys
input=sys.stdin.readline
alpha_num=[3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]

string=input().rstrip()
_sum=0
for s in string:
    _sum+=alpha_num[ord(s)-ord('A')] # 알파벳이랑 숫자랑 매칭 합니다. 
# 문제는 토너먼트 식으로 거창하게 썻는데 사실 다 더한거랑 똑같고, 홀짝 구분이기 떄문에 10으로 나눈 나머지도 필요없다
if _sum%2!=0:
    print('I\'m a winner!')
else:
    print('You\'re the winner?')