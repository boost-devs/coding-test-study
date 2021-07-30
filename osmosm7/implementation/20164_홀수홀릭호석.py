from itertools import combinations


#홀수면 1, 짝수면 0 반환
def is_odd(num):
    if num%2 ==1:
        return 1
    return 0


def count_odd(num,ct):
    global min_cnt,max_cnt
    # 숫자에 홀수 개수 확인
    for i in num:
        ct+= is_odd(int(i))

    #숫자 길이가 1이면 min, max값 갱신
    if len(num) == 1:
        if min_cnt > ct:
            min_cnt = ct
        if max_cnt < ct:
            max_cnt = ct

    #숫자 길이 2인 경우
    elif len(num) == 2:
        next_num = str(int(num[0]) + int(num[1]))
        count_odd(next_num,ct)

    #숫자의 길이가 3 이상인 경우
    else:
        # 자를 두곳 후보들을 반환
        combs = list(combinations(range(1,len(num)),2))
        for s,e in combs:
            next_num = str(int(num[:s]) +int(num[s:e])+int(num[e:]))
            count_odd(next_num,ct)

n = input()
min_cnt = 10**10
max_cnt = 0
count_odd(n,0)
print(min_cnt,max_cnt)