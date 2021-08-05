import sys
input = sys.stdin.readline

_input = input().rstrip()

r_num = 0
for s in _input:
    if s == 'R':
        r_num += 1 # r의 개수 구하기
s,e = 0, len(_input)-1 # 투 포인터
k1,k2 = 0,0 # 현재 범위의 k 개수 k1은 r을 기준으로 왼쪽의 k 개수 k2는 오른쪽의 k개수
ans = r_num # 일단 k를 다 빼면 답이 된다.
if r_num ==0 : # r이 0개면 종료
    print(0)
    sys.exit(0)
while True:
    if _input[s] == 'K': # k면 s ++ 해주고 왼쪽 k 개수를 ++
        s+=1
        k1+=1
    elif _input[e] == 'K':
        e -=1
        k2+=1
    else: # 현재 포인터가 r이면
        if k1<k2: # 왼쪽 k 개 수가 적으면 왼쪽 포인터를  ++
            s+=1
        else:
            e -=1
        r_num -= 1 # r index를 지나니 r개수 --
    if not r_num or e<s:
        break
    ans = max(ans,r_num+2*min(k1,k2)) # ans 와 r의 개수 + 좌우 k의 개수 중 최소를 더함
print(ans)