import sys
import re
from collections import defaultdict
input = sys.stdin.readline

def check_tree():
    if input_cnt+1==len(all_node) or input_cnt==0: # tree의 기본 조건인 ' 정점의 수 = 간선의 수 + 1' 을 만족해야된다.
        root=list(all_node-child_node) # root 노드를 찾는다. 단, 빈 트리일경우 root가 없다.
        if len(root)==0 or dfs(root[0]) : # 빈 트리이거나 루트에서 모든 노드로 갈 수 있는 경우를 확인한다.
            return True
    return False
def dfs(root):
    '''
        트리의 모든 노드를 순회하는 함수
        dfs로 방문한 노드 수와 트리의 노드 수가 같은지 반환해준다.
    '''
    stack=[root]
    tree_cnt=0
    while True:
        if len(stack)==0:
            return tree_cnt==len(all_node)
        node=stack.pop()
        tree_cnt+=1
        child=tree_dict[node]
        stack.extend(child)
case_num=1 # 트리 번호
Flag=True # while 문 종료 조건 입력이 -1, -1
all_node=set([]) # 트리의 모든 노드
child_node=set([]) # 트리의 자식 노드
input_cnt=0 # 간선의 수
tree_dict=defaultdict(list) # 트리
while Flag:
    values=re.split("  +", input().strip()) # '  ' 으로 입력 구분
    if values[0]=='': # \n가 입력으로 들어온 경우 제외
        continue
    for value in values:
        s,e=map(int,value.split()) # s : 시작 노드 e : 끝 노드
        if s!=0 and e!=0: # 둘다 0이 아니면
            input_cnt+=1 # 간선수 ++
            tree_dict[s].append(e) # 트리에 정보 저장
            all_node.add(s) # 노드 저장
            all_node.add(e)
            child_node.add(e) # 자식 노드 저장
        if s==0 and e==0: # s,e가 둘다 0이면 트리 입력 끝
            if check_tree():
                print('Case {} is a tree.'.format(str(case_num)))
            else:
                print('Case {} is not a tree.'.format(str(case_num)))
            # 사용한 모든 변수 초기화
            all_node=set([])
            child_node=set([])
            case_num+=1
            input_cnt=0
            tree_dict=defaultdict(list)
        # 입력값이 음수이면 종료
        elif s<=-1 and e<=-1:
            Flag=False