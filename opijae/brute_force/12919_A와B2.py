import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

def check(s,t):
    if len(s) == len(t):
        if s == t:
            return True
        else:
            return False
    if len(t)>=1:
        if t[0] =='A' and t[-1] == 'A': # t의 앞뒤가 A면 A만 빼야된다.
            return check(s,t[:-1])
        if t[0] == 'A' and t[-1] =='B': # t의 앞이 A 이며 뒤는 B가 오는 경우는 s로는 만들 수가 없다.
            return False
        if t[0] == 'B' and t[-1] =='A': #B, A 의 경우 A를 뺴는 경우와, B를 빼는 경우 둘다 되니 둘다 확인 한다,
            return (check(s,t[:-1]) or check(s,t[::-1][:-1]))
        if t[0] == 'B' and t[-1] =='B': # B, B 의 경우 B를 뺸다.
            return check(s,t[::-1][:-1])
if check(s,t):
    print(1)
else:
    print(0)