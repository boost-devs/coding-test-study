import sys

n = int(input())
n_dict = {}
for i in range(n):
    n_dict[i+1] = int(input())

# temp_dict=OrderedDict(list)
while True:
    down=set(n_dict.values())  # 밑에 배열 중복을 제거
    n_dict = {key:value for key, value in n_dict.items() if key in down} # 위의 배열과 밑에 배열과 같은 값들을 뽑기
    # print(n_dict)
    if down == set(n_dict.values()): # 밑에 배열이랑 위에 배열이 같은지 판단
        break
print(len(n_dict))
for key in n_dict.keys():
    print(key)