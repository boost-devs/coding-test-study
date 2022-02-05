def compare(x):
    x=str(x)
    return x.ljust(4,x[0])
def compare1(x):
    x=str(x)
    if len(x)>1:
        return x.ljust(4,x[1])
    return x.ljust(4,x[0])
def compare2(x):
    x=str(x)
    if len(x)>2:
        return x.ljust(4,x[2])
    return x.ljust(4,x[0])
def solution(numbers):
    answer = ''
    # 첫번째 자리로 패딩해 비교를 한다.
    # ex) (100,1000,10,20,9) -> (1001,1000,1011,2022,9999) -> (9,20,10,100,1000)
    # 첫번쨰 자리가 같다면 두번째 자리를 패딩해 비교
    # ex) (21, 212) -> (211, 212) -> (212,21)
    # 두 번쨰 자리가 같다면 세번째 자리를 패딩해 비교
    numbers=sorted(numbers ,key=lambda x: (compare(x),compare1(x),compare2(x)),reverse=True)
    answer="".join(str(x) for x in numbers)
    if answer[0]=='0':
        return '0'
    return answer