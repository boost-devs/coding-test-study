import sys
input = sys.stdin.readline

string =  input().rstrip()
answer = [""] * len(string)

def zoac(string, index):
    if string == "":
        return
    _min = 'a'

    for i in range(len(string)):  # 제일 작은 글자 & index 구하기
        if _min > string[i]:
            _min = string[i]
            next_index = i

    answer[index+next_index] = _min

    print("".join(answer))

    zoac(string[next_index+1:], index+next_index+1) # 제일 작은 값 기준 다음 문자열
    zoac(string[:next_index], index) # 제일 작은 값 기준 이전 문자열
zoac(string,0)