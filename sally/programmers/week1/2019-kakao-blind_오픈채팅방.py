# https://programmers.co.kr/learn/courses/30/lessons/42888
# 기출명: 2019 KAKAO BLIND RECRUITMENT
# 문제이름: 오픈채팅방

from collections import defaultdict

def solution(record):
    answer = []
    q = []
    id_dict = defaultdict(str)
    print_dict = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    
    for s in record:
        infos = s.split(' ')
        if s[0] == 'E':     # Enter
            q.append((infos[0], infos[1]))
            id_dict[infos[1]] = infos[2]
        elif s[0] == 'C':   # Change
            id_dict[infos[1]] = infos[2]
        elif s[0] == 'L':   # Leave
            q.append((infos[0], infos[1]))
    
    for i in q:
        answer.append(id_dict[i[1]] + print_dict[i[0]])
    
    return answer