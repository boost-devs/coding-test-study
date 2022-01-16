def solution(s):
    answer = []
    
    visited = [False for x in range(100001)]
    
    s = s[2:-2]
    sss = []
    for ss in s.split('},{'):
        sss.append(list(map(int, ss.split(','))))
    sss.sort(key=len)
    
    for i in sss:
        for j in i:
            if visited[j] is False:
                answer.append(j)
                visited[j] = True
    
    return answer