# https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    answer = ''
    ans = ['4', '1', '2']
    
    while n:
        answer = ans[n % 3] + answer
        if n % 3 == 0: # 3의 배수
            n = n // 3 - 1
        else: # 일반
            n = n // 3
        
    return answer