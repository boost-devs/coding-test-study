cnt=0

def dfs(graph,target,current_sum,idx):
    global cnt
    # index가 끝까지 갔을때 target이랑 같으면 cnt ++
    if idx==len(graph):
        if current_sum==target: 
            cnt+=1
        return
    else:
        # 더하기
        dfs(graph,target,current_sum+graph[idx],idx+1)
        # 빼기
        dfs(graph,target,current_sum-graph[idx],idx+1)

def solution(numbers, target):
    # 누적합 = 0 index = 0 부터 시작
    dfs(numbers,target,0,0)

    return cnt