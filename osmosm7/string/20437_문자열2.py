def check(sentence,num):
    if num ==1:
        return print(1,1)
    sent_len = len(sentence)
    #왼쪽에서 오른쪽으로 가면서 숫자 카운트 > k개 도달하면 갱신
    #[[위치들],갯수] > 갯수 도달하면 위치0 제거 + 갯수-=1
    max_num = -1
    min_num = 10000
    num_dict = dict()
    for i in range(len(sentence)):
        now = sentence[i]
        # 현재 문자 numdict에 없으면 추가
        if now not in num_dict.keys():
            num_dict[now] = [[i],1]
        #현재 문자 num_dict에 있으면 리스트에 위치 추가, 개수 +=1
        else:
            num_dict[now][0].append(i)
            num_dict[now][1]+=1
            #개수가 num개가 되면 길이 체크 후 갱신
            if num_dict[now][1] == num:
                dist = num_dict[now][0][-1] - num_dict[now][0][0] +1
                #print(dist,now,num_dict)
                del num_dict[now][0][0]
                num_dict[now][1] -= 1
                if dist > max_num:
                    max_num = dist
                    
                if dist < min_num:
                    min_num = dist
    if max_num == -1:
        print(-1)
    else:
        print(str(min_num)+' '+str(max_num))

T = int(input())
for i in range(T):
    sent = input()
    n = int(input())
    check(sent,n)