import sys
input = sys.stdin.readline

num_node,W = map(int,input().split())
adj_lst = [0] * (num_node+1)

for _ in range(num_node-1):
    s,e = map(int,input().split())
    adj_lst[s] += 1
    adj_lst[e] += 1
cnt = 0
for i in range(2,num_node+1):
    if adj_lst[i] == 1:
        cnt+=1
print(W/cnt)