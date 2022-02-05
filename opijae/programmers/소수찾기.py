from itertools import permutations
import math
def is_prime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True
def solution(numbers):
    answer = 0
    num_arr=[]
    # 모든 경우 만들기
    for i in range(1,len(numbers)+1):
        arr=list(map(int,map("".join,permutations(list(numbers),i))))
        num_arr.extend(arr)
    num_arr=set(num_arr) # 중복 제거
    # 각 경우가 소수인지 판단
    for num in num_arr:
        if num<2:
            continue
        if is_prime(num):
            answer+=1
    return answer