from collections import defaultdict
n,d,k,c = map(int,input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))

# 원형이므로 마지막 n번째 초밥부터의 경우도 고려할 수 있게 갱신
new_lst = lst + lst[:k-1]

# 보너스 초밥은 무조건 들어가므로 초밥 개수 1,정답 개수 1로 시작
#answer_lst = defaultdict(int)
answer_lst = [0] * (d+1)
answer_lst[c] = 1
answer = 1
now_answer = 1

for i in range(len(new_lst)):
    #answer = max(answer,len(set(new_lst[i:i+k])| set([c])))
    
    # k개가 넘어가면 기존에 처음 추가된 초밥을 제거해줌
    # 이때 제거되는 종류의 초밥이 1개 포함되어있다면 정답 갯수에서 1개 제거
    if i >=k:
        last_num = new_lst[i-k]
        if answer_lst[last_num] ==1:
            now_answer -=1 
        answer_lst[last_num] -=1
    
    num = new_lst[i]
    #현재 초밥 번호가 0개면 정답 종류 +1
    if answer_lst[num] == 0:
        now_answer +=1
    # 현재 초밥 번호 개수 +1
    answer_lst[num] += 1

    # 정답 갱신
    answer = max(answer,now_answer)
print(answer)