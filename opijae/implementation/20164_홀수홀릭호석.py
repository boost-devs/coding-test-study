import sys
from itertools import combinations
input = sys.stdin.readline

def get_odd_cnt(string):
    cnt = 0
    for s in string:
        if int(s)%2==1:
            cnt += 1
    return cnt

def split_string(string,orig,_max):
    orig = _max  # 밑에 for문을 돌릴때 _max 값을 초기화 해주지 않으면 한 자리 수에서 넘어온 _max 값에 계속해서 더해준다.
                 # EX) 999999 99 9 -> 1000107 -> .. 순으로 갈때 전 단계에서 넘어온 _max 값으로 바꿔준다.
    if len(string) >2 :
        combs = combinations([x for x in range(1,len(string)+1)],2) # 문자열을 자를 수 있는 경우의 수를 구한다.
        for a,b in combs:  # 각 문자열 마다 탐색
            _max = orig
            s1 = string[:a]
            s2 = string[a:b]
            s3 = string[b:]
            if s3 == '': # 190 -> 1,9,0 or 19,0,'' 이 나올 수 있다, 두번쨰 경우를 제외해줌
                continue
            _max += (get_odd_cnt(s1) + get_odd_cnt(s2) + get_odd_cnt(s3))
            new_string = str(int(s1)+int(s2)+int(s3))
            split_string(new_string,orig,_max)
    elif len(string) == 2:
        _max +=(get_odd_cnt(string[0]) + get_odd_cnt(string[1]))
        new_string = str(int(string[0])+int(string[1]))
        split_string(new_string,orig,_max)
    elif len(string) == 1:
        _max +=get_odd_cnt(string)
        max_list.append(_max)

string =  input().rstrip()
max_list = []
split_string(string,0,0)
print(min(max_list),max(max_list))