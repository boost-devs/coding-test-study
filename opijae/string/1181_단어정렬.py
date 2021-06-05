import sys
input = sys.stdin.readline
def compare1(x):
    '''
        길이 비교
    '''
    return len(x)
def compare2(x):
    '''
        사전순 비교
    '''
    return x
n= int(input())
word_set=set([])
for _ in range(n):
    word_set.add(input().rstrip()) # set에 add
for word in sorted(word_set,key=lambda x:(compare1(x),compare2(x))): # 문제 조건에 맞게 정렬
    print(word)