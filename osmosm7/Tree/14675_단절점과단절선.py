import sys
input = sys.stdin.readline

num_node = int(input())
adj_lst = [0] * (num_node+1)
for _ in range(num_node-1):
    s,e = map(int,input().split())
    adj_lst[s] += 1
    adj_lst[e] += 1

num_query = int(input())
for _ in range(num_query):
    a,b = map(int,input().split())
    if a ==1:
        if adj_lst[b] >1:
            print('yes')
        else:
            print('no')
    else:
        print('yes')