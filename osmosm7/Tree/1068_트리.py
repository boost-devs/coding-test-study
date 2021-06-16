def DFS(x,pass_node):
    global cnt
    #지울노드 방문하면 return
    if x == pass_node:
        return 
    # 방문한 노드가 자식이 0개라면 +=1
    elif len(adj_lst[x]) == 0:
        cnt+=1
        return

    # 핵심 : 지우는 노드의 부모 노드가 리프노드가 될때 +=1
    elif len(adj_lst[x]) ==1 and adj_lst[x][0] == pass_node:
        cnt+=1
        return
    else: 
        for i in range(len(adj_lst[x])):
            DFS(adj_lst[x][i],pass_node)
            
num_node = int(input())
node_lst = list(map(int,input().split()))  
del_node = int(input())

adj_lst = [[] for _ in range(num_node)]

for i in range(num_node):
    if node_lst[i] ==-1:
        continue
    adj_lst[node_lst[i]].append(i)
            
root_node = node_lst.index(-1)
cnt = 0
DFS(root_node,del_node)
print(cnt)