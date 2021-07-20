import sys
input = sys.stdin.readline

def calc_dist(hand,target):
    return abs(keyboard_dict[hand][0]-keyboard_dict[target][0]) + abs(keyboard_dict[hand][1]-keyboard_dict[target][1])

keyboard_dict = {}

keyboard_list = [
    ['q','w','e','r','t','y','u','i','o','p'],
    ['a','s','d','f','g','h','j','k','l'],
    ['z','x','c','v','b','n','m']
    ]
for i,row in enumerate(keyboard_list): # 키보드 dict 채우기
    for j, key in enumerate(row):
        keyboard_dict[key] = (i,j)

s_l,s_r=input().split()
string = input().rstrip()
answ=0
for s in string:
    if (keyboard_dict[s][0] <=1 and keyboard_dict[s][1] <=4) or (keyboard_dict[s][0] ==2 and keyboard_dict[s][1] <=3): # 자음이면 왼속
        answ += calc_dist(s_l,s) +1
        s_l = s
    else: #모음이면 오른손
        answ += calc_dist(s_r,s) +1
        s_r = s
print(answ)