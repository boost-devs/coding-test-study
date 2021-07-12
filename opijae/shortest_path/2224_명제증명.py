import sys
from collections import defaultdict, deque
input = sys.stdin.readline
n=int(input())
proposition_dict = defaultdict(set)
total_char=set()
for _ in range(n):
    _input = input().split()

    s,e= _input[0],_input[-1]
    if s== e:
        continue
    proposition_dict[s].add(e)
    total_char.add(s)
    total_char.add(e)
total_char=list(total_char)
length=len(total_char)
arr=[[0] * length for _ in range(length)]
sorted_total_char = sorted(total_char)
char_index_dict={x:i for i,x in enumerate(sorted_total_char)}
cnt=0
for key,items in proposition_dict.items():
    for item in items:
        i,j=char_index_dict[key],char_index_dict[item]
        arr[i][j]=1
        cnt+=1
for k in range(length):
    for i in range(length):
        for j in range(length):
            if not arr[i][j] and not i==j and arr[i][k] and arr[k][j] :
                arr[i][j]=1
                cnt+=1
print(cnt)
for i in range(length):
    for j in range(length):
        if arr[i][j]:
            print('{} => {}'.format(sorted_total_char[i],sorted_total_char[j]))